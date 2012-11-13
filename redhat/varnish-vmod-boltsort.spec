Summary: varnish-vmod-boltsort
Name: varnish-vmod-boltsort
Version: 0.1
Release: 1%{?dist}
License: Apache 2.0
Group: System Environment/Daemons
Source0: ./libvmod-boltsort.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0
BuildRequires: make, autoconf, automake, libtool, python-docutils

%description
Fast query string sorting VMOD

%prep
%setup -n libvmod-boltsort

%build
./autogen.sh
# this assumes that VARNISHSRC is defined on the rpmbuild command line, like this:
# rpmbuild -bb --define 'VARNISHSRC /home/user/rpmbuild/BUILD/varnish-3.0.3' redhat/*spec
./configure VARNISHSRC=%{VARNISHSRC} VMODDIR=/usr/lib64/varnish/vmods/ --prefix=/usr/
make

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}/ 
cp README.rst %{buildroot}/usr/share/doc/%{name}/
cp LICENSE %{buildroot}/usr/share/doc/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# /opt/varnish/lib/varnish/vmods/
/usr/lib64/varnish/vmods/
%doc /usr/share/doc/%{name}/*
%if "%{RHVERSION}" == "EL5"
%{_mandir}/man3/*.3*
%else
/usr/share/man/man?/*
%endif

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
