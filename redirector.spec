Name:           redirector
Version:        0.1
Release:        1%{?dist}
Summary:        Tests

License:        GPL
URL:            https://github.com/Fridi7/squid_redirector
Source0:        redirector-0.1.tar.gz

BuildRequires:  python3
Requires:       python3
Requires:       bash

%description
sdgsdgsdgsdgsdg

%prep
%setup -q -n SOURCES/redirector-0.1

%build

python3 -m compileall SOURCES/squid_redirector/redirector-0.1/redirector.py

%install

% define debug_package% {nil}

%files
%license LICENSE

%changelog
* Fri Jul 31 2020 root
-
