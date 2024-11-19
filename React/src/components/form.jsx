import React from "react";

function Form(){
    return(
    <div className="text-center h-96  w-full p-10">
      <form className="border w-5/12 m-auto" >
        <div>
          <label className="p-1.5 m-2  font-bold" >Name :</label>
          <input
            type="text"
            required
            className="border border-black p-1.5 rounded-lg m-2 w-8/12 bg-transparent"
          />
        </div>
        <div>
          <label className="p-1.5 m-2  font-bold">Age:</label>
          <input
            type="number"
            min={1}
            required
            className="border border-black p-1.5 rounded-lg m-2  w-8/12 bg-transparent"
          />
        </div>
        <div>
          <label className=" p-1.5 m-2 font-bold">Upload File:</label>
          <input type="file" required 
          className="border border-black p-1.5 rounded-lg m-2 w-8/12 bg-transparent"/>
        </div>
        <button type="submit" className="border border-black p-1.5 rounded-lg m-2 w-8/12 font-bold hover:bg">Submit</button>
      </form>
    </div>
    )
};

export default Form