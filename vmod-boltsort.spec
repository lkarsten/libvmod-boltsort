Summary: Fast query string sorter for Varnish %{VARNISHVER}
Name: vmod-boltsort
Version: 0.2
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-boltsort.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0
BuildRequires: make, python-docutils

%description
Fast query string sorter for Varnish VCL

%prep
%setup -n libvmod-boltsort

%build
# this assumes that VARNISHSRC is defined on the rpmbuild command line, like this:
# rpmbuild -bb --define 'VARNISHSRC /home/user/rpmbuild/BUILD/varnish-3.0.3' redhat/*spec
./configure VARNISHSRC=%{VARNISHSRC} VMODDIR="$(PKG_CONFIG_PATH=%{VARNISHSRC} pkg-config --variable=vmoddir varnishapi)" --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Mon Sep 15 2014 Lasse Karstensen <lkarsten@varnish-software.com> - 0.2-1
- Version bump due to packaging.

* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
