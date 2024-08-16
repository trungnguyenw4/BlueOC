import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPosts } from '../actions/postActions';

const PostList = () => {
  const dispatch = useDispatch();
  const posts = useSelector((state) => state.items);
  const status = useSelector((state) => state.status);
  const error = useSelector((state) => state.error);

  useEffect(() => {
    if (status === 'idle') {
      dispatch(fetchPosts());
    }
  }, [dispatch, status]);

  if (status === 'loading') {
    return <div>Loading...</div>;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  // Sort posts by ID in descending order (newest first)
  const sortedPosts = [...posts].sort((a, b) => b.id - a.id);

  return (
    <div>
      <h2>Posts</h2>
      {sortedPosts.length > 0 ? (
        sortedPosts.map((post) => (
          <div key={post.id} className="post-item">
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </div>
        ))
      ) : (
        <div>No posts available.</div>
      )}
    </div>
  );
};

export default PostList;
