import json

registree_interface = json.loads(
    r'''
    {
    "contractName": "Registree",
    "abi": [
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "address"
            }
        ],
        "name": "admins",
        "outputs": [
            {
            "name": "",
            "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "bytes32"
            }
        ],
        "name": "NftOwner",
        "outputs": [
            {
            "name": "",
            "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "bytes32"
            }
        ],
        "name": "NftAdmin",
        "outputs": [
            {
            "name": "",
            "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
            "name": "",
            "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [],
        "name": "isOwner",
        "outputs": [
            {
            "name": "",
            "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "address"
            }
        ],
        "name": "ownerNft",
        "outputs": [
            {
            "name": "",
            "type": "bytes32"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "bytes32"
            }
        ],
        "name": "queriability",
        "outputs": [
            {
            "name": "",
            "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": true,
        "inputs": [
            {
            "name": "",
            "type": "bytes32"
            }
        ],
        "name": "students",
        "outputs": [
            {
            "name": "identifyingID",
            "type": "string"
            },
            {
            "name": "identifyingURL",
            "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "newOwner",
            "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "anonymous": false,
        "inputs": [
            {
            "indexed": true,
            "name": "previousOwner",
            "type": "address"
            },
            {
            "indexed": true,
            "name": "newOwner",
            "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "_address",
            "type": "address"
            }
        ],
        "name": "registerAdmin",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "_id",
            "type": "bytes32"
            },
            {
            "name": "_identId",
            "type": "string"
            },
            {
            "name": "_identUrl",
            "type": "string"
            },
            {
            "name": "_student",
            "type": "address"
            }
        ],
        "name": "createStudent",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "_id",
            "type": "bytes32"
            },
            {
            "name": "_newOwner",
            "type": "address"
            }
        ],
        "name": "transfer",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "_id",
            "type": "bytes32"
            }
        ],
        "name": "toggleQueriability",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "constant": false,
        "inputs": [
            {
            "name": "_id",
            "type": "bytes32"
            },
            {
            "name": "_identId",
            "type": "string"
            }
        ],
        "name": "updateIdentifyingId",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
        }
    ],
    "metadata": "{\"compiler\":{\"version\":\"0.5.2+commit.1df8f40c\"},\"language\":\"Solidity\",\"output\":{\"abi\":[{\"constant\":false,\"inputs\":[{\"name\":\"_id\",\"type\":\"bytes32\"},{\"name\":\"_identId\",\"type\":\"string\"}],\"name\":\"updateIdentifyingId\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_id\",\"type\":\"bytes32\"}],\"name\":\"toggleQueriability\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"address\"}],\"name\":\"admins\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_id\",\"type\":\"bytes32\"},{\"name\":\"_identId\",\"type\":\"string\"},{\"name\":\"_identUrl\",\"type\":\"string\"},{\"name\":\"_student\",\"type\":\"address\"}],\"name\":\"createStudent\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"NftOwner\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_id\",\"type\":\"bytes32\"},{\"name\":\"_newOwner\",\"type\":\"address\"}],\"name\":\"transfer\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"NftAdmin\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"isOwner\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"address\"}],\"name\":\"ownerNft\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"}],\"name\":\"registerAdmin\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"queriability\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"students\",\"outputs\":[{\"name\":\"identifyingID\",\"type\":\"string\"},{\"name\":\"identifyingURL\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"}],\"devdoc\":{\"methods\":{\"isOwner()\":{\"return\":\"true if `msg.sender` is the owner of the contract.\"},\"owner()\":{\"return\":\"the address of the owner.\"},\"renounceOwnership()\":{\"details\":\"Allows the current owner to relinquish control of the contract. It will not be possible to call the functions with the `onlyOwner` modifier anymore.\"},\"transferOwnership(address)\":{\"details\":\"Allows the current owner to transfer control of the contract to a newOwner.\",\"params\":{\"newOwner\":\"The address to transfer ownership to.\"}}}},\"userdoc\":{\"methods\":{\"renounceOwnership()\":{\"notice\":\"Renouncing ownership will leave the contract without an owner, thereby removing any functionality that is only available to the owner.\"}}}},\"settings\":{\"compilationTarget\":{\"/home/sabine/git/studentNFT/contracts/Registree.sol\":\"Registree\"},\"evmVersion\":\"byzantium\",\"libraries\":{},\"optimizer\":{\"enabled\":false,\"runs\":200},\"remappings\":[]},\"sources\":{\"/home/sabine/git/studentNFT/contracts/Registree.sol\":{\"keccak256\":\"0x74ace8dcdc2cac84a8c9629b513edbf425d6a2deead53dda45bd686167bd4519\",\"urls\":[\"bzzr://0b7abf5bf5a56b1b6e5a21da500261642b9f2cfec73c1244f88a0f0f401f3ff8\"]},\"node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol\":{\"keccak256\":\"0xcb16adc00dcf0d75e0bdf94379f4d5a6d74dca7c74e4183b94e15721159f8a30\",\"urls\":[\"bzzr://b81e03f7203cd628cfed19255911a04a05e8670d248afb48a7b067dd03b4ff55\"]}},\"version\":1}",
    "bytecode": "0x6080604052336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36113f4806100cf6000396000f3fe608060405234801561001057600080fd5b5060043610610112576000357c0100000000000000000000000000000000000000000000000000000000900480638ab2196e116100b4578063c38c581311610083578063c38c581314610514578063c8575d4614610558578063dbf800891461059e578063f2fde38b146106b157610112565b80638ab2196e146103e25780638da5cb5b146104505780638f32d59b1461049a578063b7cdacca146104bc57610112565b8063444d8b8c116100f0578063444d8b8c146102245780634ea28c991461031c578063715018a61461038a57806379ce9fac1461039457610112565b806310994bf8146101175780632f76678a1461019a578063429b62e5146101c8575b600080fd5b6101986004803603604081101561012d57600080fd5b81019080803590602001909291908035906020019064010000000081111561015457600080fd5b82018360208201111561016657600080fd5b8035906020019184600183028401116401000000008311171561018857600080fd5b90919293919293905050506106f5565b005b6101c6600480360360208110156101b057600080fd5b8101908080359060200190929190505050610861565b005b61020a600480360360208110156101de57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109c0565b604051808215151515815260200191505060405180910390f35b61031a6004803603608081101561023a57600080fd5b81019080803590602001909291908035906020019064010000000081111561026157600080fd5b82018360208201111561027357600080fd5b8035906020019184600183028401116401000000008311171561029557600080fd5b9091929391929390803590602001906401000000008111156102b657600080fd5b8201836020820111156102c857600080fd5b803590602001918460018302840111640100000000831117156102ea57600080fd5b9091929391929390803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109e0565b005b6103486004803603602081101561033257600080fd5b8101908080359060200190929190505050610caa565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610392610cdd565b005b6103e0600480360360408110156103aa57600080fd5b8101908080359060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610daf565b005b61040e600480360360208110156103f857600080fd5b8101908080359060200190929190505050610edd565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610458610f10565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6104a2610f39565b604051808215151515815260200191505060405180910390f35b6104fe600480360360208110156104d257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610f90565b6040518082815260200191505060405180910390f35b6105566004803603602081101561052a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610fa8565b005b6105846004803603602081101561056e57600080fd5b8101908080359060200190929190505050611016565b604051808215151515815260200191505060405180910390f35b6105ca600480360360208110156105b457600080fd5b8101908080359060200190929190505050611036565b604051808060200180602001838103835285818151815260200191508051906020019080838360005b8381101561060e5780820151818401526020810190506105f3565b50505050905090810190601f16801561063b5780820380516001836020036101000a031916815260200191505b50838103825284818151815260200191508051906020019080838360005b83811015610674578082015181840152602081019050610659565b50505050905090810190601f1680156106a15780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b6106f3600480360360208110156106c757600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061118a565b005b823373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806107c157503373ffffffffffffffffffffffffffffffffffffffff166005600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b1515610835576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b828260016000878152602001908152602001600020600001919061085a9291906112a3565b5050505050565b803373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141515610938576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b6004600083815260200190815260200160002060009054906101000a900460ff161561098f5760006004600084815260200190815260200160002060006101000a81548160ff0219169083151502179055506109bc565b60016004600084815260200190815260200160002060006101000a81548160ff0219169083151502179055505b5050565b60066020528060005260406000206000915054906101000a900460ff1681565b600660003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161515610aa1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b604080519081016040528086868080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050815260200184848080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050815250600160008881526020019081526020016000206000820151816000019080519060200190610b6d929190611323565b506020820151816001019080519060200190610b8a929190611323565b50905050806002600088815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555085600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555060016004600088815260200190815260200160002060006101000a81548160ff021916908315150217905550336005600088815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050505050565b60026020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b610ce5610f39565b1515610cf057600080fd5b600073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a360008060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b813373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141515610e86576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b816002600085815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050565b60056020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614905090565b60036020528060005260406000206000915090505481565b610fb0610f39565b1515610fbb57600080fd5b6001600660008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555050565b60046020528060005260406000206000915054906101000a900460ff1681565b6001602052806000526040600020600091509050806000018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156110e25780601f106110b7576101008083540402835291602001916110e2565b820191906000526020600020905b8154815290600101906020018083116110c557829003601f168201915b505050505090806001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156111805780601f1061115557610100808354040283529160200191611180565b820191906000526020600020905b81548152906001019060200180831161116357829003601f168201915b5050505050905082565b611192610f39565b151561119d57600080fd5b6111a6816111a9565b50565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156111e557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106112e457803560ff1916838001178555611312565b82800160010185558215611312579182015b828111156113115782358255916020019190600101906112f6565b5b50905061131f91906113a3565b5090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061136457805160ff1916838001178555611392565b82800160010185558215611392579182015b82811115611391578251825591602001919060010190611376565b5b50905061139f91906113a3565b5090565b6113c591905b808211156113c15760008160009055506001016113a9565b5090565b9056fea165627a7a723058208efa5816d6e8c16b4575fcbbb13ca864382bb202b8f4ff3c9864d3e7491a2d840029",
    "deployedBytecode": "0x608060405234801561001057600080fd5b5060043610610112576000357c0100000000000000000000000000000000000000000000000000000000900480638ab2196e116100b4578063c38c581311610083578063c38c581314610514578063c8575d4614610558578063dbf800891461059e578063f2fde38b146106b157610112565b80638ab2196e146103e25780638da5cb5b146104505780638f32d59b1461049a578063b7cdacca146104bc57610112565b8063444d8b8c116100f0578063444d8b8c146102245780634ea28c991461031c578063715018a61461038a57806379ce9fac1461039457610112565b806310994bf8146101175780632f76678a1461019a578063429b62e5146101c8575b600080fd5b6101986004803603604081101561012d57600080fd5b81019080803590602001909291908035906020019064010000000081111561015457600080fd5b82018360208201111561016657600080fd5b8035906020019184600183028401116401000000008311171561018857600080fd5b90919293919293905050506106f5565b005b6101c6600480360360208110156101b057600080fd5b8101908080359060200190929190505050610861565b005b61020a600480360360208110156101de57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109c0565b604051808215151515815260200191505060405180910390f35b61031a6004803603608081101561023a57600080fd5b81019080803590602001909291908035906020019064010000000081111561026157600080fd5b82018360208201111561027357600080fd5b8035906020019184600183028401116401000000008311171561029557600080fd5b9091929391929390803590602001906401000000008111156102b657600080fd5b8201836020820111156102c857600080fd5b803590602001918460018302840111640100000000831117156102ea57600080fd5b9091929391929390803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109e0565b005b6103486004803603602081101561033257600080fd5b8101908080359060200190929190505050610caa565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610392610cdd565b005b6103e0600480360360408110156103aa57600080fd5b8101908080359060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610daf565b005b61040e600480360360208110156103f857600080fd5b8101908080359060200190929190505050610edd565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610458610f10565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6104a2610f39565b604051808215151515815260200191505060405180910390f35b6104fe600480360360208110156104d257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610f90565b6040518082815260200191505060405180910390f35b6105566004803603602081101561052a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610fa8565b005b6105846004803603602081101561056e57600080fd5b8101908080359060200190929190505050611016565b604051808215151515815260200191505060405180910390f35b6105ca600480360360208110156105b457600080fd5b8101908080359060200190929190505050611036565b604051808060200180602001838103835285818151815260200191508051906020019080838360005b8381101561060e5780820151818401526020810190506105f3565b50505050905090810190601f16801561063b5780820380516001836020036101000a031916815260200191505b50838103825284818151815260200191508051906020019080838360005b83811015610674578082015181840152602081019050610659565b50505050905090810190601f1680156106a15780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b6106f3600480360360208110156106c757600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061118a565b005b823373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806107c157503373ffffffffffffffffffffffffffffffffffffffff166005600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b1515610835576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b828260016000878152602001908152602001600020600001919061085a9291906112a3565b5050505050565b803373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141515610938576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b6004600083815260200190815260200160002060009054906101000a900460ff161561098f5760006004600084815260200190815260200160002060006101000a81548160ff0219169083151502179055506109bc565b60016004600084815260200190815260200160002060006101000a81548160ff0219169083151502179055505b5050565b60066020528060005260406000206000915054906101000a900460ff1681565b600660003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161515610aa1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b604080519081016040528086868080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050815260200184848080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050815250600160008881526020019081526020016000206000820151816000019080519060200190610b6d929190611323565b506020820151816001019080519060200190610b8a929190611323565b50905050806002600088815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555085600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555060016004600088815260200190815260200160002060006101000a81548160ff021916908315150217905550336005600088815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050505050565b60026020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b610ce5610f39565b1515610cf057600080fd5b600073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a360008060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b813373ffffffffffffffffffffffffffffffffffffffff166002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141515610e86576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f53656e64657220756e617574686f72697a65640000000000000000000000000081525060200191505060405180910390fd5b816002600085815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050565b60056020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614905090565b60036020528060005260406000206000915090505481565b610fb0610f39565b1515610fbb57600080fd5b6001600660008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555050565b60046020528060005260406000206000915054906101000a900460ff1681565b6001602052806000526040600020600091509050806000018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156110e25780601f106110b7576101008083540402835291602001916110e2565b820191906000526020600020905b8154815290600101906020018083116110c557829003601f168201915b505050505090806001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156111805780601f1061115557610100808354040283529160200191611180565b820191906000526020600020905b81548152906001019060200180831161116357829003601f168201915b5050505050905082565b611192610f39565b151561119d57600080fd5b6111a6816111a9565b50565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156111e557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106112e457803560ff1916838001178555611312565b82800160010185558215611312579182015b828111156113115782358255916020019190600101906112f6565b5b50905061131f91906113a3565b5090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061136457805160ff1916838001178555611392565b82800160010185558215611392579182015b82811115611391578251825591602001919060010190611376565b5b50905061139f91906113a3565b5090565b6113c591905b808211156113c15760008160009055506001016113a9565b5090565b9056fea165627a7a723058208efa5816d6e8c16b4575fcbbb13ca864382bb202b8f4ff3c9864d3e7491a2d840029",
    "sourceMap": "103:1756:1:-;;;524:10:2;515:6;;:19;;;;;;;;;;;;;;;;;;582:6;;;;;;;;;;;549:40;;578:1;549:40;;;;;;;;;;;;103:1756:1;;;;;;",
    "deployedSourceMap": "103:1756:1:-;;;;8:9:-1;5:2;;;30:1;27;20:12;5:2;103:1756:1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1700:156;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;1700:156:1;;;;;;;;;;;;;;;;;;;21:11:-1;8;5:28;2:2;;;46:1;43;36:12;2:2;1700:156:1;;35:9:-1;28:4;12:14;8:25;5:40;2:2;;;58:1;55;48:12;2:2;1700:156:1;;;;;;100:9:-1;95:1;81:12;77:20;67:8;63:35;60:50;39:11;25:12;22:29;11:107;8:2;;;131:1;128;121:12;8:2;1700:156:1;;;;;;;;;;;;:::i;:::-;;1483:211;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;1483:211:1;;;;;;;;;;;;;;;;;:::i;:::-;;877:39;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;877:39:1;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;1028:325;;;;;;13:3:-1;8;5:12;2:2;;;30:1;27;20:12;2:2;1028:325:1;;;;;;;;;;;;;;;;;;;21:11:-1;8;5:28;2:2;;;46:1;43;36:12;2:2;1028:325:1;;35:9:-1;28:4;12:14;8:25;5:40;2:2;;;58:1;55;48:12;2:2;1028:325:1;;;;;;100:9:-1;95:1;81:12;77:20;67:8;63:35;60:50;39:11;25:12;22:29;11:107;8:2;;;131:1;128;121:12;8:2;1028:325:1;;;;;;;;;;;;;;21:11:-1;8;5:28;2:2;;;46:1;43;36:12;2:2;1028:325:1;;35:9:-1;28:4;12:14;8:25;5:40;2:2;;;58:1;55;48:12;2:2;1028:325:1;;;;;;100:9:-1;95:1;81:12;77:20;67:8;63:35;60:50;39:11;25:12;22:29;11:107;8:2;;;131:1;128;121:12;8:2;1028:325:1;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;676:44;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;676:44:1;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;1423:137:2;;;:::i;:::-;;1359:118:1;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;1359:118:1;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;827:44;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;827:44:1;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;659:77:2;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;979:90;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;726:44:1;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;726:44:1;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;923:99;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;923:99:1;;;;;;;;;;;;;;;;;;;:::i;:::-;;776:45;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;776:45:1;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;626:44;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;626:44:1;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;23:1:-1;8:100;33:3;30:1;27:10;8:100;;;99:1;94:3;90:11;84:18;80:1;75:3;71:11;64:39;52:2;49:1;45:10;40:15;;8:100;;;12:14;626:44:1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;23:1:-1;8:100;33:3;30:1;27:10;8:100;;;99:1;94:3;90:11;84:18;80:1;75:3;71:11;64:39;52:2;49:1;45:10;40:15;;8:100;;;12:14;626:44:1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1731:107:2;;;;;;13:2:-1;8:3;5:11;2:2;;;29:1;26;19:12;2:2;1731:107:2;;;;;;;;;;;;;;;;;;;:::i;:::-;;1700:156:1;1796:3;537:10;520:27;;:8;:13;529:3;520:13;;;;;;;;;;;;;;;;;;;;;:27;;;:58;;;;568:10;551:27;;:8;:13;560:3;551:13;;;;;;;;;;;;;;;;;;;;;:27;;;520:58;512:90;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1841:8;;1811;:13;1820:3;1811:13;;;;;;;;;;;:27;;:38;;;;;;;:::i;:::-;;1700:156;;;;:::o;1483:211::-;1545:3;298:10;281:27;;:8;:13;290:3;281:13;;;;;;;;;;;;;;;;;;;;;:27;;;273:59;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1564:12;:17;1577:3;1564:17;;;;;;;;;;;;;;;;;;;;;1560:128;;;1617:5;1597:12;:17;1610:3;1597:17;;;;;;;;;;;;:25;;;;;;;;;;;;;;;;;;1560:128;;;1673:4;1653:12;:17;1666:3;1653:17;;;;;;;;;;;;:24;;;;;;;;;;;;;;;;;;1560:128;1483:211;;:::o;877:39::-;;;;;;;;;;;;;;;;;;;;;;:::o;1028:325::-;395:6;:18;402:10;395:18;;;;;;;;;;;;;;;;;;;;;;;;;387:50;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1180:28;;;;;;;;;1188:8;;1180:28;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;30:3:-1;22:6;14;1:33;99:1;93:3;85:6;81:16;74:27;137:4;133:9;126:4;121:3;117:14;113:30;106:37;;169:3;161:6;157:16;147:26;;1180:28:1;;;;;;;;;;1198:9;;1180:28;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;30:3:-1;22:6;14;1:33;99:1;93:3;85:6;81:16;74:27;137:4;133:9;126:4;121:3;117:14;113:30;106:37;;169:3;161:6;157:16;147:26;;1180:28:1;;;;;;;;;1164:8;:13;1173:3;1164:13;;;;;;;;;;;:44;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;1234:8;1218;:13;1227:3;1218:13;;;;;;;;;;;;:24;;;;;;;;;;;;;;;;;;1273:3;1252:8;:18;1261:8;1252:18;;;;;;;;;;;;;;;:24;;;;1306:4;1286:12;:17;1299:3;1286:17;;;;;;;;;;;;:24;;;;;;;;;;;;;;;;;;1336:10;1320:8;:13;1329:3;1320:13;;;;;;;;;;;;:26;;;;;;;;;;;;;;;;;;1028:325;;;;;;:::o;676:44::-;;;;;;;;;;;;;;;;;;;;;;:::o;1423:137:2:-;863:9;:7;:9::i;:::-;855:18;;;;;;;;1521:1;1484:40;;1505:6;;;;;;;;;;;1484:40;;;;;;;;;;;;1551:1;1534:6;;:19;;;;;;;;;;;;;;;;;;1423:137::o;1359:118:1:-;1430:3;298:10;281:27;;:8;:13;290:3;281:13;;;;;;;;;;;;;;;;;;;;;:27;;;273:59;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1461:9;1445:8;:13;1454:3;1445:13;;;;;;;;;;;;:25;;;;;;;;;;;;;;;;;;1359:118;;;:::o;827:44::-;;;;;;;;;;;;;;;;;;;;;;:::o;659:77:2:-;697:7;723:6;;;;;;;;;;;716:13;;659:77;:::o;979:90::-;1019:4;1056:6;;;;;;;;;;;1042:20;;:10;:20;;;1035:27;;979:90;:::o;726:44:1:-;;;;;;;;;;;;;;;;;:::o;923:99::-;863:9:2;:7;:9::i;:::-;855:18;;;;;;;;1011:4:1;992:6;:16;999:8;992:16;;;;;;;;;;;;;;;;:23;;;;;;;;;;;;;;;;;;923:99;:::o;776:45::-;;;;;;;;;;;;;;;;;;;;;;:::o;626:44::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::o;1731:107:2:-;863:9;:7;:9::i;:::-;855:18;;;;;;;;1803:28;1822:8;1803:18;:28::i;:::-;1731:107;:::o;1982:183::-;2075:1;2055:22;;:8;:22;;;;2047:31;;;;;;;;2122:8;2093:38;;2114:6;;;;;;;;;;;2093:38;;;;;;;;;;;;2150:8;2141:6;;:17;;;;;;;;;;;;;;;;;;1982:183;:::o;103:1756:1:-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;:::o",
    "source": "pragma solidity ^0.5.2;\n\nimport \"node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol\";\n\ncontract Registree is Ownable {\n\n    struct Student {\n        string identifyingID;\n        string identifyingURL;\n    }\n\n    modifier onlyStudent(bytes32 _id) {\n        require(NftOwner[_id] == msg.sender, \"Sender unauthorized\");\n        _;\n    }\n\n    modifier onlyAdmin() {\n        require(admins[msg.sender], \"Sender unauthorized\");\n        _;\n    }\n\n    modifier onlyStudentOrAdmin(bytes32 _id) {\n        require(NftOwner[_id] == msg.sender || NftAdmin[_id] == msg.sender, \"Sender unauthorized\");\n        _;\n    }\n\n    mapping (bytes32 => Student) public students;\n    mapping (bytes32 => address) public NftOwner;\n    mapping (address => bytes32) public ownerNft;\n    mapping (bytes32 => bool) public queriability;\n    mapping (bytes32 => address) public NftAdmin;\n    mapping (address => bool) public admins;\n\n    function registerAdmin(address _address) external onlyOwner{\n        admins[_address] = true;\n    }\n\n    function createStudent(bytes32 _id, string calldata _identId, string calldata _identUrl, address _student) external onlyAdmin {\n        students[_id] = Student(_identId, _identUrl);\n        NftOwner[_id] = _student;\n        ownerNft[_student] = _id;\n        queriability[_id] = true;\n        NftAdmin[_id] = msg.sender;\n    }\n\n    function transfer(bytes32 _id, address _newOwner) external onlyStudent(_id) {\n        NftOwner[_id] = _newOwner;\n    }\n\n    function toggleQueriability(bytes32 _id) external onlyStudent(_id) {\n        if (queriability[_id]) {\n            queriability[_id] = false;\n        } else {\n            queriability[_id] = true;\n        }\n    }\n\n    function updateIdentifyingId(bytes32 _id, string calldata _identId) external onlyStudentOrAdmin(_id) {\n        students[_id].identifyingID = _identId;\n    }\n\n}",
    "sourcePath": "/home/sabine/git/studentNFT/contracts/Registree.sol",
    "ast": {
        "absolutePath": "/home/sabine/git/studentNFT/contracts/Registree.sol",
        "exportedSymbols": {
        "Registree": [
            266
        ]
        },
        "id": 267,
        "nodeType": "SourceUnit",
        "nodes": [
        {
            "id": 58,
            "literals": [
            "solidity",
            "^",
            "0.5",
            ".2"
            ],
            "nodeType": "PragmaDirective",
            "src": "0:23:1"
        },
        {
            "absolutePath": "node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol",
            "file": "node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol",
            "id": 59,
            "nodeType": "ImportDirective",
            "scope": 267,
            "sourceUnit": 376,
            "src": "25:76:1",
            "symbolAliases": [],
            "unitAlias": ""
        },
        {
            "baseContracts": [
            {
                "arguments": null,
                "baseName": {
                "contractScope": null,
                "id": 60,
                "name": "Ownable",
                "nodeType": "UserDefinedTypeName",
                "referencedDeclaration": 375,
                "src": "125:7:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_contract$_Ownable_$375",
                    "typeString": "contract Ownable"
                }
                },
                "id": 61,
                "nodeType": "InheritanceSpecifier",
                "src": "125:7:1"
            }
            ],
            "contractDependencies": [
            375
            ],
            "contractKind": "contract",
            "documentation": null,
            "fullyImplemented": true,
            "id": 266,
            "linearizedBaseContracts": [
            266,
            375
            ],
            "name": "Registree",
            "nodeType": "ContractDefinition",
            "nodes": [
            {
                "canonicalName": "Registree.Student",
                "id": 66,
                "members": [
                {
                    "constant": false,
                    "id": 63,
                    "name": "identifyingID",
                    "nodeType": "VariableDeclaration",
                    "scope": 66,
                    "src": "165:20:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                    },
                    "typeName": {
                    "id": 62,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "165:6:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                    }
                    },
                    "value": null,
                    "visibility": "internal"
                },
                {
                    "constant": false,
                    "id": 65,
                    "name": "identifyingURL",
                    "nodeType": "VariableDeclaration",
                    "scope": 66,
                    "src": "195:21:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                    },
                    "typeName": {
                    "id": 64,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "195:6:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                    }
                    },
                    "value": null,
                    "visibility": "internal"
                }
                ],
                "name": "Student",
                "nodeType": "StructDefinition",
                "scope": 266,
                "src": "140:83:1",
                "visibility": "public"
            },
            {
                "body": {
                "id": 81,
                "nodeType": "Block",
                "src": "263:87:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "commonType": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            },
                            "id": 76,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                            "argumentTypes": null,
                            "baseExpression": {
                                "argumentTypes": null,
                                "id": 71,
                                "name": "NftOwner",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 125,
                                "src": "281:8:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                "typeString": "mapping(bytes32 => address)"
                                }
                            },
                            "id": 73,
                            "indexExpression": {
                                "argumentTypes": null,
                                "id": 72,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 68,
                                "src": "290:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                                }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "281:13:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                            "argumentTypes": null,
                            "expression": {
                                "argumentTypes": null,
                                "id": 74,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "298:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_magic_message",
                                "typeString": "msg"
                                }
                            },
                            "id": 75,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "memberName": "sender",
                            "nodeType": "MemberAccess",
                            "referencedDeclaration": null,
                            "src": "298:10:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                            }
                            },
                            "src": "281:27:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 77,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "310:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 70,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "273:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 78,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "273:59:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 79,
                    "nodeType": "ExpressionStatement",
                    "src": "273:59:1"
                    },
                    {
                    "id": 80,
                    "nodeType": "PlaceholderStatement",
                    "src": "342:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 82,
                "name": "onlyStudent",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 69,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 68,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 82,
                    "src": "250:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 67,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "250:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "249:13:1"
                },
                "src": "229:121:1",
                "visibility": "internal"
            },
            {
                "body": {
                "id": 93,
                "nodeType": "Block",
                "src": "377:78:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "baseExpression": {
                            "argumentTypes": null,
                            "id": 85,
                            "name": "admins",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 141,
                            "src": "395:6:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                                "typeString": "mapping(address => bool)"
                            }
                            },
                            "id": 88,
                            "indexExpression": {
                            "argumentTypes": null,
                            "expression": {
                                "argumentTypes": null,
                                "id": 86,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "402:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_magic_message",
                                "typeString": "msg"
                                }
                            },
                            "id": 87,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "memberName": "sender",
                            "nodeType": "MemberAccess",
                            "referencedDeclaration": null,
                            "src": "402:10:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                            }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "395:18:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 89,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "415:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 84,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "387:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 90,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "387:50:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 91,
                    "nodeType": "ExpressionStatement",
                    "src": "387:50:1"
                    },
                    {
                    "id": 92,
                    "nodeType": "PlaceholderStatement",
                    "src": "447:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 94,
                "name": "onlyAdmin",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 83,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "374:2:1"
                },
                "src": "356:99:1",
                "visibility": "internal"
            },
            {
                "body": {
                "id": 116,
                "nodeType": "Block",
                "src": "502:118:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "commonType": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            "id": 111,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                            "argumentTypes": null,
                            "commonType": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            },
                            "id": 104,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 99,
                                "name": "NftOwner",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 125,
                                "src": "520:8:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                    "typeString": "mapping(bytes32 => address)"
                                }
                                },
                                "id": 101,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 100,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 96,
                                "src": "529:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": false,
                                "nodeType": "IndexAccess",
                                "src": "520:13:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                                }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                                "argumentTypes": null,
                                "expression": {
                                "argumentTypes": null,
                                "id": 102,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "537:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_magic_message",
                                    "typeString": "msg"
                                }
                                },
                                "id": 103,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": false,
                                "lValueRequested": false,
                                "memberName": "sender",
                                "nodeType": "MemberAccess",
                                "referencedDeclaration": null,
                                "src": "537:10:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                                }
                            },
                            "src": "520:27:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "||",
                            "rightExpression": {
                            "argumentTypes": null,
                            "commonType": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            },
                            "id": 110,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 105,
                                "name": "NftAdmin",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 137,
                                "src": "551:8:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                    "typeString": "mapping(bytes32 => address)"
                                }
                                },
                                "id": 107,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 106,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 96,
                                "src": "560:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": false,
                                "nodeType": "IndexAccess",
                                "src": "551:13:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                                }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                                "argumentTypes": null,
                                "expression": {
                                "argumentTypes": null,
                                "id": 108,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "568:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_magic_message",
                                    "typeString": "msg"
                                }
                                },
                                "id": 109,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": false,
                                "lValueRequested": false,
                                "memberName": "sender",
                                "nodeType": "MemberAccess",
                                "referencedDeclaration": null,
                                "src": "568:10:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                                }
                            },
                            "src": "551:27:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "src": "520:58:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 112,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "580:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 98,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "512:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 113,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "512:90:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 114,
                    "nodeType": "ExpressionStatement",
                    "src": "512:90:1"
                    },
                    {
                    "id": 115,
                    "nodeType": "PlaceholderStatement",
                    "src": "612:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 117,
                "name": "onlyStudentOrAdmin",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 97,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 96,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 117,
                    "src": "489:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 95,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "489:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "488:13:1"
                },
                "src": "461:159:1",
                "visibility": "internal"
            },
            {
                "constant": false,
                "id": 121,
                "name": "students",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "626:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                "typeString": "mapping(bytes32 => struct Registree.Student)"
                },
                "typeName": {
                "id": 120,
                "keyType": {
                    "id": 118,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "635:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "626:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                    "typeString": "mapping(bytes32 => struct Registree.Student)"
                },
                "valueType": {
                    "contractScope": null,
                    "id": 119,
                    "name": "Student",
                    "nodeType": "UserDefinedTypeName",
                    "referencedDeclaration": 66,
                    "src": "646:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_struct$_Student_$66_storage_ptr",
                    "typeString": "struct Registree.Student"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 125,
                "name": "NftOwner",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "676:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
                },
                "typeName": {
                "id": 124,
                "keyType": {
                    "id": 122,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "685:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "676:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                    "typeString": "mapping(bytes32 => address)"
                },
                "valueType": {
                    "id": 123,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "696:7:1",
                    "stateMutability": "nonpayable",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 129,
                "name": "ownerNft",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "726:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                "typeString": "mapping(address => bytes32)"
                },
                "typeName": {
                "id": 128,
                "keyType": {
                    "id": 126,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "735:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                },
                "nodeType": "Mapping",
                "src": "726:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                    "typeString": "mapping(address => bytes32)"
                },
                "valueType": {
                    "id": 127,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "746:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 133,
                "name": "queriability",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "776:45:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                "typeString": "mapping(bytes32 => bool)"
                },
                "typeName": {
                "id": 132,
                "keyType": {
                    "id": 130,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "785:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "776:25:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                    "typeString": "mapping(bytes32 => bool)"
                },
                "valueType": {
                    "id": 131,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "796:4:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 137,
                "name": "NftAdmin",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "827:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
                },
                "typeName": {
                "id": 136,
                "keyType": {
                    "id": 134,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "836:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "827:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                    "typeString": "mapping(bytes32 => address)"
                },
                "valueType": {
                    "id": 135,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "847:7:1",
                    "stateMutability": "nonpayable",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 141,
                "name": "admins",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "877:39:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                "typeString": "mapping(address => bool)"
                },
                "typeName": {
                "id": 140,
                "keyType": {
                    "id": 138,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "886:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                },
                "nodeType": "Mapping",
                "src": "877:25:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                    "typeString": "mapping(address => bool)"
                },
                "valueType": {
                    "id": 139,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "897:4:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "body": {
                "id": 154,
                "nodeType": "Block",
                "src": "982:40:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 152,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 148,
                            "name": "admins",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 141,
                            "src": "992:6:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                            "typeString": "mapping(address => bool)"
                            }
                        },
                        "id": 150,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 149,
                            "name": "_address",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 143,
                            "src": "999:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "992:16:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "hexValue": "74727565",
                        "id": 151,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "bool",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "1011:4:1",
                        "subdenomination": null,
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        },
                        "value": "true"
                        },
                        "src": "992:23:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "id": 153,
                    "nodeType": "ExpressionStatement",
                    "src": "992:23:1"
                    }
                ]
                },
                "documentation": null,
                "id": 155,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": null,
                    "id": 146,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 145,
                    "name": "onlyOwner",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 309,
                    "src": "973:9:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$__$",
                        "typeString": "modifier ()"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "973:9:1"
                }
                ],
                "name": "registerAdmin",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 144,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 143,
                    "name": "_address",
                    "nodeType": "VariableDeclaration",
                    "scope": 155,
                    "src": "946:16:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 142,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "946:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "945:18:1"
                },
                "returnParameters": {
                "id": 147,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "982:0:1"
                },
                "scope": 266,
                "src": "923:99:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 202,
                "nodeType": "Block",
                "src": "1154:199:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 175,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 168,
                            "name": "students",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 121,
                            "src": "1164:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                            "typeString": "mapping(bytes32 => struct Registree.Student storage ref)"
                            }
                        },
                        "id": 170,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 169,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1173:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1164:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_storage",
                            "typeString": "struct Registree.Student storage ref"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "arguments": [
                            {
                            "argumentTypes": null,
                            "id": 172,
                            "name": "_identId",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 159,
                            "src": "1188:8:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            },
                            {
                            "argumentTypes": null,
                            "id": 173,
                            "name": "_identUrl",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 161,
                            "src": "1198:9:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            }
                        ],
                        "expression": {
                            "argumentTypes": [
                            {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            },
                            {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            ],
                            "id": 171,
                            "name": "Student",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 66,
                            "src": "1180:7:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_type$_t_struct$_Student_$66_storage_ptr_$",
                            "typeString": "type(struct Registree.Student storage pointer)"
                            }
                        },
                        "id": 174,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "structConstructorCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "1180:28:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_memory",
                            "typeString": "struct Registree.Student memory"
                        }
                        },
                        "src": "1164:44:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_struct$_Student_$66_storage",
                        "typeString": "struct Registree.Student storage ref"
                        }
                    },
                    "id": 176,
                    "nodeType": "ExpressionStatement",
                    "src": "1164:44:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 181,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 177,
                            "name": "NftOwner",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "1218:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 179,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 178,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1227:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1218:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 180,
                        "name": "_student",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 163,
                        "src": "1234:8:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "src": "1218:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 182,
                    "nodeType": "ExpressionStatement",
                    "src": "1218:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 187,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 183,
                            "name": "ownerNft",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 129,
                            "src": "1252:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                            "typeString": "mapping(address => bytes32)"
                            }
                        },
                        "id": 185,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 184,
                            "name": "_student",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 163,
                            "src": "1261:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1252:18:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 186,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 157,
                        "src": "1273:3:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "src": "1252:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "id": 188,
                    "nodeType": "ExpressionStatement",
                    "src": "1252:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 193,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 189,
                            "name": "queriability",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 133,
                            "src": "1286:12:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                            "typeString": "mapping(bytes32 => bool)"
                            }
                        },
                        "id": 191,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 190,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1299:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1286:17:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "hexValue": "74727565",
                        "id": 192,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "bool",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "1306:4:1",
                        "subdenomination": null,
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        },
                        "value": "true"
                        },
                        "src": "1286:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "id": 194,
                    "nodeType": "ExpressionStatement",
                    "src": "1286:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 200,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 195,
                            "name": "NftAdmin",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 137,
                            "src": "1320:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 197,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 196,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1329:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1320:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "expression": {
                            "argumentTypes": null,
                            "id": 198,
                            "name": "msg",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 390,
                            "src": "1336:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_magic_message",
                            "typeString": "msg"
                            }
                        },
                        "id": 199,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "sender",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": null,
                        "src": "1336:10:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address_payable",
                            "typeString": "address payable"
                        }
                        },
                        "src": "1320:26:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 201,
                    "nodeType": "ExpressionStatement",
                    "src": "1320:26:1"
                    }
                ]
                },
                "documentation": null,
                "id": 203,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": null,
                    "id": 166,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 165,
                    "name": "onlyAdmin",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 94,
                    "src": "1144:9:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$__$",
                        "typeString": "modifier ()"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1144:9:1"
                }
                ],
                "name": "createStudent",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 164,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 157,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1051:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 156,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1051:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 159,
                    "name": "_identId",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1064:24:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 158,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1064:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 161,
                    "name": "_identUrl",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1090:25:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 160,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1090:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 163,
                    "name": "_student",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1117:16:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 162,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "1117:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1050:84:1"
                },
                "returnParameters": {
                "id": 167,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1154:0:1"
                },
                "scope": 266,
                "src": "1028:325:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 219,
                "nodeType": "Block",
                "src": "1435:42:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 217,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 213,
                            "name": "NftOwner",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "1445:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 215,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 214,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 205,
                            "src": "1454:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1445:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 216,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 207,
                        "src": "1461:9:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "src": "1445:25:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 218,
                    "nodeType": "ExpressionStatement",
                    "src": "1445:25:1"
                    }
                ]
                },
                "documentation": null,
                "id": 220,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 210,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 205,
                        "src": "1430:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 211,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 209,
                    "name": "onlyStudent",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 82,
                    "src": "1418:11:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1418:16:1"
                }
                ],
                "name": "transfer",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 208,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 205,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 220,
                    "src": "1377:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 204,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1377:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 207,
                    "name": "_newOwner",
                    "nodeType": "VariableDeclaration",
                    "scope": 220,
                    "src": "1390:17:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 206,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "1390:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1376:32:1"
                },
                "returnParameters": {
                "id": 212,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1435:0:1"
                },
                "scope": 266,
                "src": "1359:118:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 246,
                "nodeType": "Block",
                "src": "1550:144:1",
                "statements": [
                    {
                    "condition": {
                        "argumentTypes": null,
                        "baseExpression": {
                        "argumentTypes": null,
                        "id": 228,
                        "name": "queriability",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 133,
                        "src": "1564:12:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                            "typeString": "mapping(bytes32 => bool)"
                        }
                        },
                        "id": 230,
                        "indexExpression": {
                        "argumentTypes": null,
                        "id": 229,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 222,
                        "src": "1577:3:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "1564:17:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "falseBody": {
                        "id": 244,
                        "nodeType": "Block",
                        "src": "1639:49:1",
                        "statements": [
                        {
                            "expression": {
                            "argumentTypes": null,
                            "id": 242,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftHandSide": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 238,
                                "name": "queriability",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 133,
                                "src": "1653:12:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                                    "typeString": "mapping(bytes32 => bool)"
                                }
                                },
                                "id": 240,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 239,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 222,
                                "src": "1666:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": true,
                                "nodeType": "IndexAccess",
                                "src": "1653:17:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                }
                            },
                            "nodeType": "Assignment",
                            "operator": "=",
                            "rightHandSide": {
                                "argumentTypes": null,
                                "hexValue": "74727565",
                                "id": 241,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": true,
                                "kind": "bool",
                                "lValueRequested": false,
                                "nodeType": "Literal",
                                "src": "1673:4:1",
                                "subdenomination": null,
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                },
                                "value": "true"
                            },
                            "src": "1653:24:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "id": 243,
                            "nodeType": "ExpressionStatement",
                            "src": "1653:24:1"
                        }
                        ]
                    },
                    "id": 245,
                    "nodeType": "IfStatement",
                    "src": "1560:128:1",
                    "trueBody": {
                        "id": 237,
                        "nodeType": "Block",
                        "src": "1583:50:1",
                        "statements": [
                        {
                            "expression": {
                            "argumentTypes": null,
                            "id": 235,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftHandSide": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 231,
                                "name": "queriability",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 133,
                                "src": "1597:12:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                                    "typeString": "mapping(bytes32 => bool)"
                                }
                                },
                                "id": 233,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 232,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 222,
                                "src": "1610:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": true,
                                "nodeType": "IndexAccess",
                                "src": "1597:17:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                }
                            },
                            "nodeType": "Assignment",
                            "operator": "=",
                            "rightHandSide": {
                                "argumentTypes": null,
                                "hexValue": "66616c7365",
                                "id": 234,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": true,
                                "kind": "bool",
                                "lValueRequested": false,
                                "nodeType": "Literal",
                                "src": "1617:5:1",
                                "subdenomination": null,
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                },
                                "value": "false"
                            },
                            "src": "1597:25:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "id": 236,
                            "nodeType": "ExpressionStatement",
                            "src": "1597:25:1"
                        }
                        ]
                    }
                    }
                ]
                },
                "documentation": null,
                "id": 247,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 225,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 222,
                        "src": "1545:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 226,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 224,
                    "name": "onlyStudent",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 82,
                    "src": "1533:11:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1533:16:1"
                }
                ],
                "name": "toggleQueriability",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 223,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 222,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 247,
                    "src": "1511:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 221,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1511:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1510:13:1"
                },
                "returnParameters": {
                "id": 227,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1550:0:1"
                },
                "scope": 266,
                "src": "1483:211:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 264,
                "nodeType": "Block",
                "src": "1801:55:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 262,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "expression": {
                            "argumentTypes": null,
                            "baseExpression": {
                            "argumentTypes": null,
                            "id": 257,
                            "name": "students",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 121,
                            "src": "1811:8:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                                "typeString": "mapping(bytes32 => struct Registree.Student storage ref)"
                            }
                            },
                            "id": 259,
                            "indexExpression": {
                            "argumentTypes": null,
                            "id": 258,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 249,
                            "src": "1820:3:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                            }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "1811:13:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_storage",
                            "typeString": "struct Registree.Student storage ref"
                            }
                        },
                        "id": 260,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "memberName": "identifyingID",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 63,
                        "src": "1811:27:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_string_storage",
                            "typeString": "string storage ref"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 261,
                        "name": "_identId",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 251,
                        "src": "1841:8:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_string_calldata_ptr",
                            "typeString": "string calldata"
                        }
                        },
                        "src": "1811:38:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage",
                        "typeString": "string storage ref"
                        }
                    },
                    "id": 263,
                    "nodeType": "ExpressionStatement",
                    "src": "1811:38:1"
                    }
                ]
                },
                "documentation": null,
                "id": 265,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 254,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 249,
                        "src": "1796:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 255,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 253,
                    "name": "onlyStudentOrAdmin",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 117,
                    "src": "1777:18:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1777:23:1"
                }
                ],
                "name": "updateIdentifyingId",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 252,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 249,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 265,
                    "src": "1729:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 248,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1729:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 251,
                    "name": "_identId",
                    "nodeType": "VariableDeclaration",
                    "scope": 265,
                    "src": "1742:24:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 250,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1742:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1728:39:1"
                },
                "returnParameters": {
                "id": 256,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1801:0:1"
                },
                "scope": 266,
                "src": "1700:156:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            }
            ],
            "scope": 267,
            "src": "103:1756:1"
        }
        ],
        "src": "0:1859:1"
    },
    "legacyAST": {
        "absolutePath": "/home/sabine/git/studentNFT/contracts/Registree.sol",
        "exportedSymbols": {
        "Registree": [
            266
        ]
        },
        "id": 267,
        "nodeType": "SourceUnit",
        "nodes": [
        {
            "id": 58,
            "literals": [
            "solidity",
            "^",
            "0.5",
            ".2"
            ],
            "nodeType": "PragmaDirective",
            "src": "0:23:1"
        },
        {
            "absolutePath": "node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol",
            "file": "node_modules/openzeppelin-solidity/contracts/ownership/Ownable.sol",
            "id": 59,
            "nodeType": "ImportDirective",
            "scope": 267,
            "sourceUnit": 376,
            "src": "25:76:1",
            "symbolAliases": [],
            "unitAlias": ""
        },
        {
            "baseContracts": [
            {
                "arguments": null,
                "baseName": {
                "contractScope": null,
                "id": 60,
                "name": "Ownable",
                "nodeType": "UserDefinedTypeName",
                "referencedDeclaration": 375,
                "src": "125:7:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_contract$_Ownable_$375",
                    "typeString": "contract Ownable"
                }
                },
                "id": 61,
                "nodeType": "InheritanceSpecifier",
                "src": "125:7:1"
            }
            ],
            "contractDependencies": [
            375
            ],
            "contractKind": "contract",
            "documentation": null,
            "fullyImplemented": true,
            "id": 266,
            "linearizedBaseContracts": [
            266,
            375
            ],
            "name": "Registree",
            "nodeType": "ContractDefinition",
            "nodes": [
            {
                "canonicalName": "Registree.Student",
                "id": 66,
                "members": [
                {
                    "constant": false,
                    "id": 63,
                    "name": "identifyingID",
                    "nodeType": "VariableDeclaration",
                    "scope": 66,
                    "src": "165:20:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                    },
                    "typeName": {
                    "id": 62,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "165:6:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                    }
                    },
                    "value": null,
                    "visibility": "internal"
                },
                {
                    "constant": false,
                    "id": 65,
                    "name": "identifyingURL",
                    "nodeType": "VariableDeclaration",
                    "scope": 66,
                    "src": "195:21:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                    },
                    "typeName": {
                    "id": 64,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "195:6:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                    }
                    },
                    "value": null,
                    "visibility": "internal"
                }
                ],
                "name": "Student",
                "nodeType": "StructDefinition",
                "scope": 266,
                "src": "140:83:1",
                "visibility": "public"
            },
            {
                "body": {
                "id": 81,
                "nodeType": "Block",
                "src": "263:87:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "commonType": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            },
                            "id": 76,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                            "argumentTypes": null,
                            "baseExpression": {
                                "argumentTypes": null,
                                "id": 71,
                                "name": "NftOwner",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 125,
                                "src": "281:8:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                "typeString": "mapping(bytes32 => address)"
                                }
                            },
                            "id": 73,
                            "indexExpression": {
                                "argumentTypes": null,
                                "id": 72,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 68,
                                "src": "290:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                                }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "281:13:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                            "argumentTypes": null,
                            "expression": {
                                "argumentTypes": null,
                                "id": 74,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "298:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_magic_message",
                                "typeString": "msg"
                                }
                            },
                            "id": 75,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "memberName": "sender",
                            "nodeType": "MemberAccess",
                            "referencedDeclaration": null,
                            "src": "298:10:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                            }
                            },
                            "src": "281:27:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 77,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "310:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 70,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "273:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 78,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "273:59:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 79,
                    "nodeType": "ExpressionStatement",
                    "src": "273:59:1"
                    },
                    {
                    "id": 80,
                    "nodeType": "PlaceholderStatement",
                    "src": "342:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 82,
                "name": "onlyStudent",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 69,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 68,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 82,
                    "src": "250:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 67,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "250:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "249:13:1"
                },
                "src": "229:121:1",
                "visibility": "internal"
            },
            {
                "body": {
                "id": 93,
                "nodeType": "Block",
                "src": "377:78:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "baseExpression": {
                            "argumentTypes": null,
                            "id": 85,
                            "name": "admins",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 141,
                            "src": "395:6:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                                "typeString": "mapping(address => bool)"
                            }
                            },
                            "id": 88,
                            "indexExpression": {
                            "argumentTypes": null,
                            "expression": {
                                "argumentTypes": null,
                                "id": 86,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "402:3:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_magic_message",
                                "typeString": "msg"
                                }
                            },
                            "id": 87,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "memberName": "sender",
                            "nodeType": "MemberAccess",
                            "referencedDeclaration": null,
                            "src": "402:10:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                            }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "395:18:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 89,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "415:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 84,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "387:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 90,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "387:50:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 91,
                    "nodeType": "ExpressionStatement",
                    "src": "387:50:1"
                    },
                    {
                    "id": 92,
                    "nodeType": "PlaceholderStatement",
                    "src": "447:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 94,
                "name": "onlyAdmin",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 83,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "374:2:1"
                },
                "src": "356:99:1",
                "visibility": "internal"
            },
            {
                "body": {
                "id": 116,
                "nodeType": "Block",
                "src": "502:118:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "arguments": [
                        {
                            "argumentTypes": null,
                            "commonType": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            "id": 111,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                            "argumentTypes": null,
                            "commonType": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            },
                            "id": 104,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 99,
                                "name": "NftOwner",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 125,
                                "src": "520:8:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                    "typeString": "mapping(bytes32 => address)"
                                }
                                },
                                "id": 101,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 100,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 96,
                                "src": "529:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": false,
                                "nodeType": "IndexAccess",
                                "src": "520:13:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                                }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                                "argumentTypes": null,
                                "expression": {
                                "argumentTypes": null,
                                "id": 102,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "537:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_magic_message",
                                    "typeString": "msg"
                                }
                                },
                                "id": 103,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": false,
                                "lValueRequested": false,
                                "memberName": "sender",
                                "nodeType": "MemberAccess",
                                "referencedDeclaration": null,
                                "src": "537:10:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                                }
                            },
                            "src": "520:27:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "||",
                            "rightExpression": {
                            "argumentTypes": null,
                            "commonType": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                            },
                            "id": 110,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftExpression": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 105,
                                "name": "NftAdmin",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 137,
                                "src": "551:8:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                    "typeString": "mapping(bytes32 => address)"
                                }
                                },
                                "id": 107,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 106,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 96,
                                "src": "560:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": false,
                                "nodeType": "IndexAccess",
                                "src": "551:13:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                                }
                            },
                            "nodeType": "BinaryOperation",
                            "operator": "==",
                            "rightExpression": {
                                "argumentTypes": null,
                                "expression": {
                                "argumentTypes": null,
                                "id": 108,
                                "name": "msg",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 390,
                                "src": "568:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_magic_message",
                                    "typeString": "msg"
                                }
                                },
                                "id": 109,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": false,
                                "lValueRequested": false,
                                "memberName": "sender",
                                "nodeType": "MemberAccess",
                                "referencedDeclaration": null,
                                "src": "568:10:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_address_payable",
                                "typeString": "address payable"
                                }
                            },
                            "src": "551:27:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "src": "520:58:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            }
                        },
                        {
                            "argumentTypes": null,
                            "hexValue": "53656e64657220756e617574686f72697a6564",
                            "id": 112,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "kind": "string",
                            "lValueRequested": false,
                            "nodeType": "Literal",
                            "src": "580:21:1",
                            "subdenomination": null,
                            "typeDescriptions": {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            },
                            "value": "Sender unauthorized"
                        }
                        ],
                        "expression": {
                        "argumentTypes": [
                            {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                            },
                            {
                            "typeIdentifier": "t_stringliteral_b6bb237fb4b3f9f6fd431bdd5e5af2427314237a6aa4a8a352c5b461fa641b45",
                            "typeString": "literal_string \"Sender unauthorized\""
                            }
                        ],
                        "id": 98,
                        "name": "require",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [
                            393,
                            394
                        ],
                        "referencedDeclaration": 394,
                        "src": "512:7:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                            "typeString": "function (bool,string memory) pure"
                        }
                        },
                        "id": 113,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "512:90:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_tuple$__$",
                        "typeString": "tuple()"
                        }
                    },
                    "id": 114,
                    "nodeType": "ExpressionStatement",
                    "src": "512:90:1"
                    },
                    {
                    "id": 115,
                    "nodeType": "PlaceholderStatement",
                    "src": "612:1:1"
                    }
                ]
                },
                "documentation": null,
                "id": 117,
                "name": "onlyStudentOrAdmin",
                "nodeType": "ModifierDefinition",
                "parameters": {
                "id": 97,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 96,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 117,
                    "src": "489:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 95,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "489:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "488:13:1"
                },
                "src": "461:159:1",
                "visibility": "internal"
            },
            {
                "constant": false,
                "id": 121,
                "name": "students",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "626:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                "typeString": "mapping(bytes32 => struct Registree.Student)"
                },
                "typeName": {
                "id": 120,
                "keyType": {
                    "id": 118,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "635:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "626:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                    "typeString": "mapping(bytes32 => struct Registree.Student)"
                },
                "valueType": {
                    "contractScope": null,
                    "id": 119,
                    "name": "Student",
                    "nodeType": "UserDefinedTypeName",
                    "referencedDeclaration": 66,
                    "src": "646:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_struct$_Student_$66_storage_ptr",
                    "typeString": "struct Registree.Student"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 125,
                "name": "NftOwner",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "676:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
                },
                "typeName": {
                "id": 124,
                "keyType": {
                    "id": 122,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "685:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "676:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                    "typeString": "mapping(bytes32 => address)"
                },
                "valueType": {
                    "id": 123,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "696:7:1",
                    "stateMutability": "nonpayable",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 129,
                "name": "ownerNft",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "726:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                "typeString": "mapping(address => bytes32)"
                },
                "typeName": {
                "id": 128,
                "keyType": {
                    "id": 126,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "735:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                },
                "nodeType": "Mapping",
                "src": "726:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                    "typeString": "mapping(address => bytes32)"
                },
                "valueType": {
                    "id": 127,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "746:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 133,
                "name": "queriability",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "776:45:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                "typeString": "mapping(bytes32 => bool)"
                },
                "typeName": {
                "id": 132,
                "keyType": {
                    "id": 130,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "785:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "776:25:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                    "typeString": "mapping(bytes32 => bool)"
                },
                "valueType": {
                    "id": 131,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "796:4:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 137,
                "name": "NftAdmin",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "827:44:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
                },
                "typeName": {
                "id": 136,
                "keyType": {
                    "id": 134,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "836:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                    }
                },
                "nodeType": "Mapping",
                "src": "827:28:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                    "typeString": "mapping(bytes32 => address)"
                },
                "valueType": {
                    "id": 135,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "847:7:1",
                    "stateMutability": "nonpayable",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "constant": false,
                "id": 141,
                "name": "admins",
                "nodeType": "VariableDeclaration",
                "scope": 266,
                "src": "877:39:1",
                "stateVariable": true,
                "storageLocation": "default",
                "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                "typeString": "mapping(address => bool)"
                },
                "typeName": {
                "id": 140,
                "keyType": {
                    "id": 138,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "886:7:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                    }
                },
                "nodeType": "Mapping",
                "src": "877:25:1",
                "typeDescriptions": {
                    "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                    "typeString": "mapping(address => bool)"
                },
                "valueType": {
                    "id": 139,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "897:4:1",
                    "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                    }
                }
                },
                "value": null,
                "visibility": "public"
            },
            {
                "body": {
                "id": 154,
                "nodeType": "Block",
                "src": "982:40:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 152,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 148,
                            "name": "admins",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 141,
                            "src": "992:6:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_bool_$",
                            "typeString": "mapping(address => bool)"
                            }
                        },
                        "id": 150,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 149,
                            "name": "_address",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 143,
                            "src": "999:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "992:16:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "hexValue": "74727565",
                        "id": 151,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "bool",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "1011:4:1",
                        "subdenomination": null,
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        },
                        "value": "true"
                        },
                        "src": "992:23:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "id": 153,
                    "nodeType": "ExpressionStatement",
                    "src": "992:23:1"
                    }
                ]
                },
                "documentation": null,
                "id": 155,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": null,
                    "id": 146,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 145,
                    "name": "onlyOwner",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 309,
                    "src": "973:9:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$__$",
                        "typeString": "modifier ()"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "973:9:1"
                }
                ],
                "name": "registerAdmin",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 144,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 143,
                    "name": "_address",
                    "nodeType": "VariableDeclaration",
                    "scope": 155,
                    "src": "946:16:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 142,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "946:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "945:18:1"
                },
                "returnParameters": {
                "id": 147,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "982:0:1"
                },
                "scope": 266,
                "src": "923:99:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 202,
                "nodeType": "Block",
                "src": "1154:199:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 175,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 168,
                            "name": "students",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 121,
                            "src": "1164:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                            "typeString": "mapping(bytes32 => struct Registree.Student storage ref)"
                            }
                        },
                        "id": 170,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 169,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1173:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1164:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_storage",
                            "typeString": "struct Registree.Student storage ref"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "arguments": [
                            {
                            "argumentTypes": null,
                            "id": 172,
                            "name": "_identId",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 159,
                            "src": "1188:8:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            },
                            {
                            "argumentTypes": null,
                            "id": 173,
                            "name": "_identUrl",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 161,
                            "src": "1198:9:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            }
                        ],
                        "expression": {
                            "argumentTypes": [
                            {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            },
                            {
                                "typeIdentifier": "t_string_calldata_ptr",
                                "typeString": "string calldata"
                            }
                            ],
                            "id": 171,
                            "name": "Student",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 66,
                            "src": "1180:7:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_type$_t_struct$_Student_$66_storage_ptr_$",
                            "typeString": "type(struct Registree.Student storage pointer)"
                            }
                        },
                        "id": 174,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "structConstructorCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "1180:28:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_memory",
                            "typeString": "struct Registree.Student memory"
                        }
                        },
                        "src": "1164:44:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_struct$_Student_$66_storage",
                        "typeString": "struct Registree.Student storage ref"
                        }
                    },
                    "id": 176,
                    "nodeType": "ExpressionStatement",
                    "src": "1164:44:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 181,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 177,
                            "name": "NftOwner",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "1218:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 179,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 178,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1227:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1218:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 180,
                        "name": "_student",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 163,
                        "src": "1234:8:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "src": "1218:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 182,
                    "nodeType": "ExpressionStatement",
                    "src": "1218:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 187,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 183,
                            "name": "ownerNft",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 129,
                            "src": "1252:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_bytes32_$",
                            "typeString": "mapping(address => bytes32)"
                            }
                        },
                        "id": 185,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 184,
                            "name": "_student",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 163,
                            "src": "1261:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1252:18:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 186,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 157,
                        "src": "1273:3:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "src": "1252:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "id": 188,
                    "nodeType": "ExpressionStatement",
                    "src": "1252:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 193,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 189,
                            "name": "queriability",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 133,
                            "src": "1286:12:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                            "typeString": "mapping(bytes32 => bool)"
                            }
                        },
                        "id": 191,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 190,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1299:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1286:17:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "hexValue": "74727565",
                        "id": 192,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "bool",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "1306:4:1",
                        "subdenomination": null,
                        "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                        },
                        "value": "true"
                        },
                        "src": "1286:24:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "id": 194,
                    "nodeType": "ExpressionStatement",
                    "src": "1286:24:1"
                    },
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 200,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 195,
                            "name": "NftAdmin",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 137,
                            "src": "1320:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 197,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 196,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 157,
                            "src": "1329:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1320:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "expression": {
                            "argumentTypes": null,
                            "id": 198,
                            "name": "msg",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 390,
                            "src": "1336:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_magic_message",
                            "typeString": "msg"
                            }
                        },
                        "id": 199,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "sender",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": null,
                        "src": "1336:10:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address_payable",
                            "typeString": "address payable"
                        }
                        },
                        "src": "1320:26:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 201,
                    "nodeType": "ExpressionStatement",
                    "src": "1320:26:1"
                    }
                ]
                },
                "documentation": null,
                "id": 203,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": null,
                    "id": 166,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 165,
                    "name": "onlyAdmin",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 94,
                    "src": "1144:9:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$__$",
                        "typeString": "modifier ()"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1144:9:1"
                }
                ],
                "name": "createStudent",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 164,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 157,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1051:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 156,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1051:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 159,
                    "name": "_identId",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1064:24:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 158,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1064:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 161,
                    "name": "_identUrl",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1090:25:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 160,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1090:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 163,
                    "name": "_student",
                    "nodeType": "VariableDeclaration",
                    "scope": 203,
                    "src": "1117:16:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 162,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "1117:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1050:84:1"
                },
                "returnParameters": {
                "id": 167,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1154:0:1"
                },
                "scope": 266,
                "src": "1028:325:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 219,
                "nodeType": "Block",
                "src": "1435:42:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 217,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "baseExpression": {
                            "argumentTypes": null,
                            "id": 213,
                            "name": "NftOwner",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "1445:8:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                            "typeString": "mapping(bytes32 => address)"
                            }
                        },
                        "id": 215,
                        "indexExpression": {
                            "argumentTypes": null,
                            "id": 214,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 205,
                            "src": "1454:3:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                            }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "nodeType": "IndexAccess",
                        "src": "1445:13:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 216,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 207,
                        "src": "1461:9:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                        }
                        },
                        "src": "1445:25:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "id": 218,
                    "nodeType": "ExpressionStatement",
                    "src": "1445:25:1"
                    }
                ]
                },
                "documentation": null,
                "id": 220,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 210,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 205,
                        "src": "1430:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 211,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 209,
                    "name": "onlyStudent",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 82,
                    "src": "1418:11:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1418:16:1"
                }
                ],
                "name": "transfer",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 208,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 205,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 220,
                    "src": "1377:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 204,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1377:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 207,
                    "name": "_newOwner",
                    "nodeType": "VariableDeclaration",
                    "scope": 220,
                    "src": "1390:17:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                    },
                    "typeName": {
                        "id": 206,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "1390:7:1",
                        "stateMutability": "nonpayable",
                        "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1376:32:1"
                },
                "returnParameters": {
                "id": 212,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1435:0:1"
                },
                "scope": 266,
                "src": "1359:118:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 246,
                "nodeType": "Block",
                "src": "1550:144:1",
                "statements": [
                    {
                    "condition": {
                        "argumentTypes": null,
                        "baseExpression": {
                        "argumentTypes": null,
                        "id": 228,
                        "name": "queriability",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 133,
                        "src": "1564:12:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                            "typeString": "mapping(bytes32 => bool)"
                        }
                        },
                        "id": 230,
                        "indexExpression": {
                        "argumentTypes": null,
                        "id": 229,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 222,
                        "src": "1577:3:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                        }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "1564:17:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                        }
                    },
                    "falseBody": {
                        "id": 244,
                        "nodeType": "Block",
                        "src": "1639:49:1",
                        "statements": [
                        {
                            "expression": {
                            "argumentTypes": null,
                            "id": 242,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftHandSide": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 238,
                                "name": "queriability",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 133,
                                "src": "1653:12:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                                    "typeString": "mapping(bytes32 => bool)"
                                }
                                },
                                "id": 240,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 239,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 222,
                                "src": "1666:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": true,
                                "nodeType": "IndexAccess",
                                "src": "1653:17:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                }
                            },
                            "nodeType": "Assignment",
                            "operator": "=",
                            "rightHandSide": {
                                "argumentTypes": null,
                                "hexValue": "74727565",
                                "id": 241,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": true,
                                "kind": "bool",
                                "lValueRequested": false,
                                "nodeType": "Literal",
                                "src": "1673:4:1",
                                "subdenomination": null,
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                },
                                "value": "true"
                            },
                            "src": "1653:24:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "id": 243,
                            "nodeType": "ExpressionStatement",
                            "src": "1653:24:1"
                        }
                        ]
                    },
                    "id": 245,
                    "nodeType": "IfStatement",
                    "src": "1560:128:1",
                    "trueBody": {
                        "id": 237,
                        "nodeType": "Block",
                        "src": "1583:50:1",
                        "statements": [
                        {
                            "expression": {
                            "argumentTypes": null,
                            "id": 235,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": false,
                            "lValueRequested": false,
                            "leftHandSide": {
                                "argumentTypes": null,
                                "baseExpression": {
                                "argumentTypes": null,
                                "id": 231,
                                "name": "queriability",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 133,
                                "src": "1597:12:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_bytes32_$_t_bool_$",
                                    "typeString": "mapping(bytes32 => bool)"
                                }
                                },
                                "id": 233,
                                "indexExpression": {
                                "argumentTypes": null,
                                "id": 232,
                                "name": "_id",
                                "nodeType": "Identifier",
                                "overloadedDeclarations": [],
                                "referencedDeclaration": 222,
                                "src": "1610:3:1",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_bytes32",
                                    "typeString": "bytes32"
                                }
                                },
                                "isConstant": false,
                                "isLValue": true,
                                "isPure": false,
                                "lValueRequested": true,
                                "nodeType": "IndexAccess",
                                "src": "1597:17:1",
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                }
                            },
                            "nodeType": "Assignment",
                            "operator": "=",
                            "rightHandSide": {
                                "argumentTypes": null,
                                "hexValue": "66616c7365",
                                "id": 234,
                                "isConstant": false,
                                "isLValue": false,
                                "isPure": true,
                                "kind": "bool",
                                "lValueRequested": false,
                                "nodeType": "Literal",
                                "src": "1617:5:1",
                                "subdenomination": null,
                                "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                                },
                                "value": "false"
                            },
                            "src": "1597:25:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bool",
                                "typeString": "bool"
                            }
                            },
                            "id": 236,
                            "nodeType": "ExpressionStatement",
                            "src": "1597:25:1"
                        }
                        ]
                    }
                    }
                ]
                },
                "documentation": null,
                "id": 247,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 225,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 222,
                        "src": "1545:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 226,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 224,
                    "name": "onlyStudent",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 82,
                    "src": "1533:11:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1533:16:1"
                }
                ],
                "name": "toggleQueriability",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 223,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 222,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 247,
                    "src": "1511:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 221,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1511:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1510:13:1"
                },
                "returnParameters": {
                "id": 227,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1550:0:1"
                },
                "scope": 266,
                "src": "1483:211:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            },
            {
                "body": {
                "id": 264,
                "nodeType": "Block",
                "src": "1801:55:1",
                "statements": [
                    {
                    "expression": {
                        "argumentTypes": null,
                        "id": 262,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftHandSide": {
                        "argumentTypes": null,
                        "expression": {
                            "argumentTypes": null,
                            "baseExpression": {
                            "argumentTypes": null,
                            "id": 257,
                            "name": "students",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 121,
                            "src": "1811:8:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_struct$_Student_$66_storage_$",
                                "typeString": "mapping(bytes32 => struct Registree.Student storage ref)"
                            }
                            },
                            "id": 259,
                            "indexExpression": {
                            "argumentTypes": null,
                            "id": 258,
                            "name": "_id",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 249,
                            "src": "1820:3:1",
                            "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                            }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "1811:13:1",
                            "typeDescriptions": {
                            "typeIdentifier": "t_struct$_Student_$66_storage",
                            "typeString": "struct Registree.Student storage ref"
                            }
                        },
                        "id": 260,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": true,
                        "memberName": "identifyingID",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 63,
                        "src": "1811:27:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_string_storage",
                            "typeString": "string storage ref"
                        }
                        },
                        "nodeType": "Assignment",
                        "operator": "=",
                        "rightHandSide": {
                        "argumentTypes": null,
                        "id": 261,
                        "name": "_identId",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 251,
                        "src": "1841:8:1",
                        "typeDescriptions": {
                            "typeIdentifier": "t_string_calldata_ptr",
                            "typeString": "string calldata"
                        }
                        },
                        "src": "1811:38:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage",
                        "typeString": "string storage ref"
                        }
                    },
                    "id": 263,
                    "nodeType": "ExpressionStatement",
                    "src": "1811:38:1"
                    }
                ]
                },
                "documentation": null,
                "id": 265,
                "implemented": true,
                "kind": "function",
                "modifiers": [
                {
                    "arguments": [
                    {
                        "argumentTypes": null,
                        "id": 254,
                        "name": "_id",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 249,
                        "src": "1796:3:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    }
                    ],
                    "id": 255,
                    "modifierName": {
                    "argumentTypes": null,
                    "id": 253,
                    "name": "onlyStudentOrAdmin",
                    "nodeType": "Identifier",
                    "overloadedDeclarations": [],
                    "referencedDeclaration": 117,
                    "src": "1777:18:1",
                    "typeDescriptions": {
                        "typeIdentifier": "t_modifier$_t_bytes32_$",
                        "typeString": "modifier (bytes32)"
                    }
                    },
                    "nodeType": "ModifierInvocation",
                    "src": "1777:23:1"
                }
                ],
                "name": "updateIdentifyingId",
                "nodeType": "FunctionDefinition",
                "parameters": {
                "id": 252,
                "nodeType": "ParameterList",
                "parameters": [
                    {
                    "constant": false,
                    "id": 249,
                    "name": "_id",
                    "nodeType": "VariableDeclaration",
                    "scope": 265,
                    "src": "1729:11:1",
                    "stateVariable": false,
                    "storageLocation": "default",
                    "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                    },
                    "typeName": {
                        "id": 248,
                        "name": "bytes32",
                        "nodeType": "ElementaryTypeName",
                        "src": "1729:7:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    },
                    {
                    "constant": false,
                    "id": 251,
                    "name": "_identId",
                    "nodeType": "VariableDeclaration",
                    "scope": 265,
                    "src": "1742:24:1",
                    "stateVariable": false,
                    "storageLocation": "calldata",
                    "typeDescriptions": {
                        "typeIdentifier": "t_string_calldata_ptr",
                        "typeString": "string"
                    },
                    "typeName": {
                        "id": 250,
                        "name": "string",
                        "nodeType": "ElementaryTypeName",
                        "src": "1742:6:1",
                        "typeDescriptions": {
                        "typeIdentifier": "t_string_storage_ptr",
                        "typeString": "string"
                        }
                    },
                    "value": null,
                    "visibility": "internal"
                    }
                ],
                "src": "1728:39:1"
                },
                "returnParameters": {
                "id": 256,
                "nodeType": "ParameterList",
                "parameters": [],
                "src": "1801:0:1"
                },
                "scope": 266,
                "src": "1700:156:1",
                "stateMutability": "nonpayable",
                "superFunction": null,
                "visibility": "external"
            }
            ],
            "scope": 267,
            "src": "103:1756:1"
        }
        ],
        "src": "0:1859:1"
    },
    "compiler": {
        "name": "solc",
        "version": "0.5.2+commit.1df8f40c.Emscripten.clang"
    },
    "networks": {
        "5777": {
        "events": {
            "0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0": {
            "anonymous": false,
            "inputs": [
                {
                "indexed": true,
                "name": "previousOwner",
                "type": "address"
                },
                {
                "indexed": true,
                "name": "newOwner",
                "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event",
            "signature": "0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0"
            }
        },
        "links": {},
        "address": "0xb04625C7eF91Ce8016074E8D7D3cf84acf06c355",
        "transactionHash": "0xac9ef2d129dab2e33325587463f14dcbbf5f3d02b060b127b6b51244e157eb2f"
        }
    },
    "schemaVersion": "3.0.6",
    "updatedAt": "2019-04-18T08:37:56.689Z",
    "devdoc": {
        "methods": {
        "isOwner()": {
            "return": "true if `msg.sender` is the owner of the contract."
        },
        "owner()": {
            "return": "the address of the owner."
        },
        "renounceOwnership()": {
            "details": "Allows the current owner to relinquish control of the contract. It will not be possible to call the functions with the `onlyOwner` modifier anymore."
        },
        "transferOwnership(address)": {
            "details": "Allows the current owner to transfer control of the contract to a newOwner.",
            "params": {
            "newOwner": "The address to transfer ownership to."
            }
        }
        }
    },
    "userdoc": {
        "methods": {
        "renounceOwnership()": {
            "notice": "Renouncing ownership will leave the contract without an owner, thereby removing any functionality that is only available to the owner."
        }
        }
    }
    }
    '''
)