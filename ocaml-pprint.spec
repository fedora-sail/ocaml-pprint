Name:           ocaml-pprint
Version:        20230830
Release:        %autorelease
Summary:        A pretty-printing combinator library for OCaml

License:        LGPL-2.0-only
URL:            https://github.com/fpottier/pprint
Source0:        https://github.com/fpottier/pprint/archive/%{version}/pprint-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7

%description
PPrint is an OCaml library for pretty-printing textual documents. It takes care of indentation and line breaks, and is typically used to pretty-print code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n pprint-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
