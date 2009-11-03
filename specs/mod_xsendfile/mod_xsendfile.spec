# $Id$
# Authority: dag

Summary: Apache2 module that processes X-SENDFILE headers
Name: mod_xsendfile
Version: 0.9
Release: 1%{?dist}
License: Apache License, Version 2.0
Group: System Environment/Daemons
URL: http://tn123.ath.cx/mod_xsendfile/

Source: http://tn123.ath.cx/mod_xsendfile/mod_xsendfile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel
BuildRequires: httpd-devel
Requires: httpd

%description
mod_xsendfile is a small Apache2 module that processes X-SENDFILE headers
registered by the original output handler.

If it encounters the presence of such header it will discard all output and
send the file specified by that header instead using Apache internals
including all optimizations like caching-headers and sendfile or mmap if
configured.

It is useful for processing script-output of e.g. php, perl or any cgi.


%prep
%setup

%{__cat} <<EOF >mod_xsendfile.conf
### Load the module
LoadModule xsendfile_module         modules/mod_xsendfile.so

### Enables or disables header processing, default is disabled
XSendFile on

### Allows or disallows sending files above Request path, default is off
### Setting XSendFileAllowAbove on will allow sending files not below
### the path of the Request (this refers to the request URI not the
### translated path).
XSendFileAllowAbove off
EOF

%build
%{_sbindir}/apxs -c mod_xsendfile.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 .libs/mod_xsendfile.so %{buildroot}%{_libdir}/httpd/modules/mod_xsendfile.so
%{__install} -Dp -m0644 mod_xsendfile.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_xsendfile.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Readme.html
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_xsendfile.conf
%{_libdir}/httpd/modules/mod_xsendfile.so

%changelog
* Thu Mar 19 2009 Serdar Bulut <serdar_bulut@phoenix.com> - 0.9-1
- Initial package.
