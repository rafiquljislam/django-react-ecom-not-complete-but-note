export const initialState = {
    token: null, // SET_TOKEN
    products: null, // SET_PRODUCT 
    catagory: null, //  SET_CATAGORY
    cart: null, // SET_CART
    cartproducts: null, // SET_CARTPRODUCTS
    order: null, // SET_ORDER
    profile: null, // SET_PROFILE
    user: null // SET_USER
}

const reducer = (state, action) => {
    console.log(action.type);
    switch (action.type) {
        case "SET_TOKEN":
            return {
                ...state,
                token: action.token
            };
        case "SET_PRODUCT":
            return {
                ...state,
                products: action.products
            };
        case "SET_PROFILE":
            return {
                ...state,
                profile: action.profile
            };
        case "SET_USER":
            return {
                ...state,
                user: action.user
            };
        case "SET_CART":
            return {
                ...state,
                cart: action.cart
            };
    }
}
export default reducer;