Name:           redirector
Version:        0.1
Release:        1%{?dist}
Summary:        Squid proxy redirector

License:        MIT
URL:            https://github.com/Fridi7/squid_redirector
Source0:        redirector-0.1.tar.gz


BuildRequires:  python
Requires:       python
Requires:       bash

BuildArch:      noarch  

%description
Squid proxy redirector that redirects requests to specified sites.
For example, there is a list of redirects of the form "key": "value" ("yandex.ru": "google.com").
You should replace /etc/squid/squid.conf with squid.conf from this package.

%prep
%autosetup


%build
%py3_compile


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}
chmod 0755 %{buildroot}/%{_bindir}/%{name}


rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/etc/squid



%changelog
* Sat Aug  1 2020 root
- First redirector package
