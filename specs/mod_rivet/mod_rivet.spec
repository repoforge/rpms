# $Id$
# Authority: yury
# Upstream: Apache Rivet team <rivet-dev$tcl,apache,org>

%define real_name rivet

Summary: Apache Rivet lets you use the Tcl scripting language to create dynamic web sites
Name: mod_rivet
Version: 2.0.4
Release: 1%{?dist}
License: Apache License Version 2.0
Group: Development/Languages
URL: http://tcl.apache.org/rivet/

Source0: http://www.apache.org/dist/tcl/%{real_name}/%{real_name}-%{version}.tar.gz
Source1: http://www.apache.org/dist/tcl/%{real_name}/%{real_name}-%{version}.tar.gz.asc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: httpd-devel >= 2.0.46-1
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: tcl >= 8.4
BuildRequires: tcl-devel >= 8.4

Requires: httpd
Requires: tcl >= 8.4

%description
Tcl is a scripting language.  Apache Rivet is a module for Apache
httpd that makes it easy easy for developers to write dynamically
generated webpages in Tcl.

%prep
%setup -q -n rivet-%{version}

%build

%configure \
    --with-apxs="%{_sbindir}/apxs"       \
    --with-apache="%{_prefix}"           \
    --with-apache-version="2"            \
    --with-rivet-target-dir="%{_libdir}/httpd/rivet%{version}"   \
    --with-pic \
    --disable-rpath

%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} doc


%install

%{__make} install DESTDIR=%{buildroot}

# Remove static libraries
rm -f %{buildroot}%{_libdir}/httpd/modules/mod_rivet.la
rm -f %{buildroot}%{_libdir}/httpd/rivet%{version}/librivet*.la

# Create an Apache conf include
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
cat <<EOT >%{buildroot}%{_sysconfdir}/httpd/conf.d/rivet.conf

# Loads the module
LoadModule rivet_module modules/mod_rivet.so

# Let the module handle .rvt and .tcl files
AddType application/x-httpd-rivet  rvt
AddType application/x-rivet-tcl    tcl

# The default charset can be specified in the configuration
AddType "application/x-httpd-rivet; charset=utf-8" rvt

# Add index.rvt to the list of files that will be served
DirectoryIndex index.rvt

EOT


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE NOTICE contrib doc/html doc/examples
%config(noreplace) %{_sysconfdir}/httpd/conf.d/rivet.conf
%{_libdir}/httpd/modules/mod_rivet.so
%{_libdir}/httpd/rivet%{version}


%changelog
* Thu Oct 6 2011 Jeff Lawson <jeff@bovine.net> - 2.0.4-1
- Updated to release 2.0.4.

* Thu Aug 11 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.3-1
- Regenerating the build system is no longer necessary.
- Rivet can be built against TCL 8.4, so why not?
- Merged the updated version from Jeff.

* Mon May 03 2010 Yury V. Zaytsev <yury@shurup.com> - 2.0.0-1
- Merged the updated version from Jeff.

* Thu Apr 15 2010 Yury V. Zaytsev <yury@shurup.com> - 0.8.0-0.20100414032008.1
- Initial import of the SPEC by Jeff Lawson <jeff$bovine,net>, thanks!
- Minor RPMForge-related tweaks.
