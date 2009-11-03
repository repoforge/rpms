# $Id$
# Authority: matthias

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?dtag: %{expand: %%define %dtag 1}}
%{?rh7:  %define _without_python 1}

Summary: Persistent SQL database connection library and daemon
Name: squale
Version: 0.1.10
Release: 0.3%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://sourceforge.net/projects/squale/
Source0: http://dl.sf.net/squale/squale-%{version}.tar.gz
Source1: squale_check.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/ldconfig, /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /usr/sbin/userdel, /usr/sbin/groupdel, /sbin/ldconfig, /sbin/service
# Version this one since lib requirements can be met but problems will arise
# at runtime and make squale crash
Requires: glib2 >= 2.2.0
BuildRequires: glib2-devel >= 2.2.0, libxml2-devel, pkgconfig, gettext, popt
BuildRequires: perl(XML::Parser)
%{?_with_oracle:BuildRequires: libsqlora8-devel >= 2.3.1}
%{!?_without_mysql:BuildRequires: mysql-devel}
%{!?_without_postgresql:BuildRequires: postgresql-devel}

%description
SQuaLe, persistent SQL database connection library and daemon.

Available rpmbuild rebuild options :
--with : oracle
--without : mysql postgresql


%package devel
Summary: Development headers and library for SQuaLe
Group: Development/Libraries
Requires: %{name} = %{version}, glib2-devel, libxml2-devel, pkgconfig

%description devel
Development headers and library for SQuaLe.


%package -n python-squale
Summary: Python bindings for SQuaLe
Group: System Environment/Daemons
Requires: %{name} = %{version}, python
%{!?_without_python:BuildRequires: Pyrex, python-devel, python}

%description -n python-squale
Python module which provides bindings to the SQuaLe persistent SQL database
connection library.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Change the default log file
%{__perl} -pi -e 's|"/.*log"|"%{_var}/log/squale/squale.log"|g' \
    %{buildroot}%{_sysconfdir}/squale.xml
%{__mkdir_p} %{buildroot}%{_var}/log/squale

# Install the init script
%{__install} -D -p -m 0755 contrib/squale.init \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/squale

# Install the logrotate entry
%{__install} -D -p -m 0644 contrib/squale.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/squale

# Install the monitoring check script
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}%{_bindir}/squale_check.py


%clean
%{__rm} -rf %{buildroot}


%pre
# Create system account
/usr/sbin/useradd -c "SQuaLe" -r -M -d / -s '' squale &>/dev/null || :

%post
/sbin/ldconfig
/sbin/chkconfig --add squale

%preun
if [ $1 -eq 0 ]; then
    # Last removal, stop service and remove it
    /sbin/service squale stop &>/dev/null || :
    /sbin/chkconfig --del squale
fi

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    # Last removal, remove system account and matching group
    /usr/sbin/userdel squale &>/dev/null || :
    /usr/sbin/groupdel squale &>/dev/null || :
else
    /sbin/service squale condrestart &>/dev/null || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc conf/squale.xml
%attr(0640, root, squale) %config(noreplace) %{_sysconfdir}/squale.xml
%config %{_sysconfdir}/logrotate.d/squale
%{_sysconfdir}/rc.d/init.d/squale
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man?/*
%attr(0770, root, squale) %{_var}/log/squale

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%if %{!?_without_python:1}0
%files -n python-squale
%defattr(-, root, root, 0755)
%exclude %{python_sitearch}/squale.a
%exclude %{python_sitearch}/squale.la
%{python_sitearch}/squale.so
%{python_sitelib}/SQuaLe.py*
%endif


%changelog
* Wed Oct  4 2006 Matthias Saou <http://freshrpms.net/> 0.1.10-0.3
- Update to 0.1.10 pre-version.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.9-1
- Update to 0.1.9.
- Add new SQuaLe.py* files to the python sub-package.

* Tue Mar 14 2006 Matthias Saou <http://freshrpms.net/> 0.1.6-1
- Update to 0.1.6 final.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 0.1.6-0
- Update to 0.1.6 pre-release (fix for client timeouts).

* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 0.1.5-2
- Split off the python bindings.
- Remove redundant CFLAGS export.
- Minor spec file cleanups.

* Thu Jun 23 2005 Matthias Saou <http://freshrpms.net/> 0.1.5-1
- Update to 0.1.5.

* Fri Apr 15 2005 Matthias Saou <http://freshrpms.net/> 0.1.4-2
- Remove -fPIC forcing, as tests show it now works as expected (the shared lib
  is built with -fPIC, the rest isn't).

* Thu Apr 14 2005 Matthias Saou <http://freshrpms.net/> 0.1.4-1
- Update to 0.1.4 (fixes NLS_LANG problem & reconnection problems).

* Tue Apr 12 2005 Matthias Saou <http://freshrpms.net/> 0.1.3-2
- Added glib2-devel to devel package requirements.
- Build with -fPIC to fix x86_64 build.

* Wed Jan 12 2005 Matthias Saou <http://freshrpms.net/> 0.1.3-1
- Update to 0.1.3.

* Tue Jan  4 2005 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Update to 0.1.2.

* Tue Nov 30 2004 Matthias Saou <http://freshrpms.net/> 0.1.1-1
- Changed python to be conditional, and disable on rh7.

* Thu Nov 25 2004 Matthias Saou <http://freshrpms.net/> 0.1.1-1
- Update to 0.1.1.

* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net/> 0.1.0-1
- Update to 0.1.0.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.0.9-1
- Update to 0.0.9.
- Included python bindings.

* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 0.0.8-1
- Update to 0.0.8.

* Thu Oct 14 2004 Matthias Saou <http://freshrpms.net/> 0.0.7-1
- Update to 0.0.7.

* Fri Oct  1 2004 Matthias Saou <http://freshrpms.net/> 0.0.6-1
- Update to 0.0.6.

* Tue Sep 28 2004 Matthias Saou <http://freshrpms.net/> 0.0.5-1
- Update to 0.0.5.

* Thu Sep  2 2004 Matthias Saou <http://freshrpms.net/> 0.0.4-5
- Recompile against Oracle 9i libs (was 8i previously).

* Thu May 27 2004 Matthias Saou <http://freshrpms.net/> 0.0.4-2
- Decided to finally include the monitoring check in the package directly.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.0.4-1
- Update to 0.0.4.

* Tue Apr 27 2004 Matthias Saou <http://freshrpms.net/> 0.0.2-1
- Update to 0.0.2.

* Fri Mar 26 2004 Matthias Saou <http://freshrpms.net/> 0.0.1-1
- Initial RPM release.

