# $Id$

Summary: Persistent SQL database connection libarary and daemon
Name: squale
Version: 0.1.1
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://squale.sourceforge.net/
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
BuildRequires: Pyrex, python-devel, python
BuildRequires: perl(XML::Parser), gcc-c++
%{?_with_oracle:BuildRequires: libsqlora8-devel >= 2.2.0}
%{!?_without_mysql:BuildRequires: mysql-devel}
%{!?_without_postgresql:BuildRequires: postgresql-devel}

%description
SQuaLe.

Available rpmbuild rebuild options :
--with : oracle
--without : mysql postgresql


%package devel
Summary: Development headers and library for SQuaLe
Group: Development/Libraries
Requires: %{name} = %{version}, libxml2-devel, pkgconfig

%description devel
Development headers and library for SQuaLe.


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
%{__perl} -pi -e 's|"/.*log"|"%{_localstatedir}/log/squale/squale.log"|g' \
    %{buildroot}%{_sysconfdir}/squale.xml
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/squale

# Install the init script
%{__install} -m 0755 -D contrib/squale.init \
    %{buildroot}%{_initrddir}/squale

# Install the logrotate entry
%{__install} -m 0644 -D contrib/squale.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/squale

# Install the monitoring check script
%{__install} -m 0755 -D %{SOURCE1} \
    %{buildroot}%{_bindir}/squale_check.py


%clean
%{__rm} -rf %{buildroot}


%pre
# Create system account
/usr/sbin/useradd -c "SQuaLe" -r -M -d / -s '' squale >/dev/null 2>&1 || :

%post
/sbin/ldconfig
/sbin/chkconfig --add squale

%preun
if [ $1 -eq 0 ]; then
    # Last removal, stop service and remove it
    /sbin/service squale stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del squale
fi

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    # Last removal, remove system account and matching group
    /usr/sbin/userdel squale >/dev/null 2>&1 || :
    /usr/sbin/groupdel squale >/dev/null 2>&1 || :
else
    /sbin/service squale condrestart >/dev/null 2>&1 || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc conf/squale.xml
%attr(0640, root, squale) %config(noreplace) %{_sysconfdir}/squale.xml
%config %{_sysconfdir}/logrotate.d/squale
%{_initrddir}/squale
%{_bindir}/*
%exclude %{_libdir}/python?.?/site-packages/squale.a
%exclude %{_libdir}/python?.?/site-packages/squale.la
%{_libdir}/python?.?/site-packages/squale.so
%{_libdir}/*.so.*
%{_mandir}/man?/*
%attr(0770, root, squale) %{_localstatedir}/log/squale

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
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

