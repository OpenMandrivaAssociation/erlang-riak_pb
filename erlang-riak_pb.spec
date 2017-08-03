%global realname riak_pb
%global upstream basho
# Techincally, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	2.1.2.0
Release:	%mkrel 6
Summary:	Riak Protocol Buffers Messages
Group:		Development/Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_pb-0001-Proper-version-in-app-file.patch
# FIXME add Python and Java bindings
BuildRequires:	erlang-hamcrest
BuildRequires:	erlang-protobuffs >= 0.7.0
BuildRequires:	erlang-rebar


%description
The message definitions for the Protocol Buffers-based interface to Riak and
various Erlang-specific utility modules for the message types.


%prep
%setup -q -n %{realname}-%{version}
%patch1 -p1


%build
%{rebar_compile}


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/{ebin,include}
install -m 644 ebin/%{realname}.app ebin/*.beam %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin
install -m 644 include/*.hrl %{buildroot}%{_erllibdir}/%{realname}-%{version}/include


%files
%license LICENSE
%doc README.md
%{_erllibdir}/%{realname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 2.1.2.0-6.mga6
+ Revision: 1010454
- imported package erlang-riak_pb

