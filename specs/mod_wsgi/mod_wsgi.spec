# $Id$
# Authority: dfateyev

### RHEL6 comes with 3.2-1
%{?el6:# Tag: rfx}

Name: mod_wsgi
Version: 3.4
Release: 1%{?dist}
Summary: A WSGI interface for Python web applications in Apache

Group: System Environment/Libraries
License: ASL 2.0
URL: http://modwsgi.org
Source0: http://modwsgi.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: wsgi.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: httpd-devel
BuildRequires: python-devel


%description
The mod_wsgi adapter is an Apache module that provides a WSGI compliant
interface for hosting Python based web applications within Apache. The
adapter is written completely in C code against the Apache C runtime and
for hosting WSGI applications within Apache has a lower overhead than using
existing WSGI adapters for mod_python or CGI.


%prep
%setup


%build
%configure --enable-shared
%{__make} LDFLAGS="-L%{_libdir}" %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__install} -d -m 755 %{buildroot}/%{_sysconfdir}/httpd/conf.d
%{__install} -p -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/httpd/conf.d/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENCE README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/wsgi.conf
%{_libdir}/httpd/modules/mod_wsgi.so


%changelog
* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 3.4-1
- Update to 3.4
- Rebuild for Repoforge

* Mon Nov 07 2011 Josh <jokajak@fedoraproject.org> 3.2-2
- backport patch to support SSL options in 3.2 see bz719411

* Tue Mar  9 2010 Josh Kayse <josh.kayse@gtri.gatech.edu> 3.2-1
- update to 3.2
- explicitly enable shared libraries
- add a comment block to the configuration informing the administrator of 
  incompatibilities between mod_python and mod_wsgi
- update the configuration to disable mod_wsgi until the administrator enables

* Thu Jul 02 2009 James Bowes <jbowes@redhat.com> 2.5-1
- Update to 2.5

* Wed Oct 08 2008 James Bowes <jbowes@redhat.com> 2.1-2
- Remove requires on httpd-devel

* Wed Jul 02 2008 James Bowes <jbowes@redhat.com> 2.1-1
- Update to 2.1

* Mon Jun 16 2008 Ricky Zhou <ricky@fedoraproject.org> 1.3-4
- Build against the shared python lib.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-3
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 James Bowes <jbowes@redhat.com> 1.3-2
- Require httpd

* Sat Jan 05 2008 James Bowes <jbowes@redhat.com> 1.3-1
- Update to 1.3

* Sun Sep 30 2007 James Bowes <jbowes@redhat.com> 1.0-1
- Initial packaging for Fedora

