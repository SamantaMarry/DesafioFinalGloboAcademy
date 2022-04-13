import { useCallback, useEffect, useState } from "react";

export const useFetch = (asyncFunction, immediate = true) => {
  //"idle" | "pending" | "success" | "error"
  const [status, setStatus] = useState("idle");
  const [value, setValue] = useState(null);
  const [error, setError] = useState(null);

  const execute = useCallback(() => {
    setStatus("pending");
    setValue(null);
    setError(null);

    return asyncFunction()
      .then((response) => {
        setValue(response);
        setStatus("success");
      })
      .catch((error) => {
        setError(error);
        setStatus("error");
      });
  }, [asyncFunction]);

  useEffect(() => {
    if (immediate) {
      execute();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [immediate]);

  return { execute, status, value, error };
};

/**
 * EXEMPLO DE USO
 * 
 * const { value, status } = useAsync(() => getMedia('movie'));
 * 
 * export const getMedia = async (type: string) => {
 *    const response = await fetch(`${process.env.REACT_APP_API_URL}/discover/${type}?api_key=${process.env.REACT_APP_API_KEY}`);
 *    const data = await response.json();
 *    return data.results;
 * }
 * 
 * ---
 * 
 * import { useAsync } from "../../hooks/useAsync";
 * import { ListMedia } from "../../components/ListMedia";
 * import { getMedia } from "../../api/getMedia";
 * import { Loading } from "../../components/Loading";
 * 
 * function Movies() {
 *    const { value, status } = useAsync(() => getMedia('movie'));
 *   
 *    if (status === "pending") {
 *        return <Loading />
 *    }
 *
 *     return <ListMedia mediaData={value} />
 * }
 *
 * export default Movies;
 */