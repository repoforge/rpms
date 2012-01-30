# ExclusiveDist: el5 el6

Summary: Ganglia Distributed Monitoring System
Name: ganglia
Version: 3.1.7
Release: 3%{?dist}
License: BSD
Group: Applications/Internet
URL: http://ganglia.sourceforge.net/

Source0: http://dl.sf.net/project/ganglia/ganglia%20monitoring%20core/%{version}/ganglia-%{version}.tar.gz
#Source0: http://dl.sf.net/sourceforge/ganglia/ganglia-%{version}.tar.gz
#Source0: http://www.ganglia.info/snapshots/3.1.x/ganglia-%{version}.%{svnrev}.tar.gz
Patch0: diskusage-pcre.patch
Patch1: setuserid-fix.patch
Patch2: diskmetrics.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel >= 1
BuildRequires: expat-devel
BuildRequires: freetype-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libconfuse-devel
BuildRequires: libpng-devel
BuildRequires: pcre-devel
BuildRequires: python-devel
BuildRequires: rrdtool-devel

%description
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

%package web
Summary: Ganglia Web Frontend
Group: Applications/Internet
Requires: rrdtool
Requires: php
Requires: php-gd
Requires: ganglia-gmetad = %{version}-%{release}

%description web
This package provides a web frontend to display the XML tree published by
ganglia, and to provide historical graphs of collected metrics. This website is
written in the PHP4 language.

%package gmetad
Summary: Ganglia Metadata collection daemon
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description gmetad
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmetad daemon aggregates monitoring data from several clusters
to form a monitoring grid. It also keeps metric history using rrdtool.

%package gmond
Summary: Ganglia Monitoring daemon
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmond daemon provides the ganglia service within a single cluster or
Multicast domain.

%package gmond-python
Summary: Ganglia Monitor daemon python DSO and metric modules
Group: Applications/Internet
Requires: ganglia-gmond, python

%description gmond-python
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This package provides the gmond python DSO and python gmond modules, which
can be loaded via the DSO at gmond daemon start time.

%package devel
Summary: Ganglia Library
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}

%description devel
The Ganglia Monitoring Core library provides a set of functions that
programmers can use to build scalable cluster or grid applications

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
## Hey, those shouldn't be executable...
chmod -x lib/*.{h,x}

%build
%configure \
    --disable-static \
    --enable-shared \
    --sysconfdir="%{_sysconfdir}/ganglia" \
    --enable-setuid="ganglia" \
    --enable-setgid="ganglia" \
    --with-gmetad

## Default to run as user ganglia instead of nobody
%{__perl} -pi.orig -e 's|nobody|ganglia|g' \
    gmond/gmond.conf.html ganglia.html gmond/conf.pod

## Don't have initscripts turn daemons on by default
%{__perl} -pi.orig -e 's|2345|-|g' \
    gmond/gmond.init gmetad/gmetad.init

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

## Put web files in place
%{__install} -d -m0755 %{buildroot}%{_datadir}/ganglia/
%{__cp} -rp web/* %{buildroot}%{_datadir}/ganglia/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/ganglia/
%{__mv} %{buildroot}%{_datadir}/ganglia/conf.php %{buildroot}%{_sysconfdir}/ganglia/
%{__ln_s} ../../..%{_sysconfdir}/ganglia/conf.php \
    %{buildroot}%{_datadir}/ganglia/conf.php
%{__mv} %{buildroot}%{_datadir}/ganglia/private_clusters %{buildroot}%{_sysconfdir}/ganglia/
%{__ln_s} ../../..%{_sysconfdir}/ganglia/private_clusters \
    %{buildroot}%{_datadir}/ganglia/private_clusters

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d/
cat <<EOF >%{buildroot}%{_sysconfdir}/httpd/conf.d/ganglia.conf
#
# Ganglia monitoring system php web frontend
#

Alias /ganglia %{_datadir}/ganglia

<Location /ganglia>
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    Allow from ::1
    # Allow from .example.com
</Location>
EOF

## Create directory structures
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/ganglia/rrds/
## Put files in place
%{__install} -Dp -m0755 gmond/gmond.init %{buildroot}%{_sysconfdir}/init.d/gmond
%{__install} -Dp -m0755 gmetad/gmetad.init %{buildroot}%{_sysconfdir}/init.d/gmetad
%{__install} -Dp -m0644 gmond/gmond.conf.5 %{buildroot}%{_mandir}/man5/gmond.conf.5
%{__install} -Dp -m0644 gmetad/gmetad.conf %{buildroot}%{_sysconfdir}/ganglia/gmetad.conf
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -Dp -m0644 mans/*.1 %{buildroot}%{_mandir}/man1/
## Build default gmond.conf from gmond using the '-t' flag
gmond/gmond -t | %{__perl} -pe 's|nobody|ganglia|g' > %{buildroot}%{_sysconfdir}/ganglia/gmond.conf

## Python bits
# Copy the python metric modules and .conf files
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/ganglia/conf.d/
%{__install} -p -m0644 gmond/python_modules/conf.d/*.pyconf %{buildroot}%{_sysconfdir}/ganglia/conf.d/
%{__install} -p -m0644 gmond/modules/conf.d/*.conf %{buildroot}%{_sysconfdir}/ganglia/conf.d/
%{__install} -d -m0755 %{buildroot}%{_libdir}/ganglia/python_modules/
%{__install} -p -m0644 gmond/python_modules/*/*.py %{buildroot}%{_libdir}/ganglia/python_modules/
# Don't install the example modules
%{__rm} -f %{buildroot}%{_sysconfdir}/ganglia/conf.d/example.conf
%{__rm} -f %{buildroot}%{_sysconfdir}/ganglia/conf.d/example.pyconf
# Don't install the status modules
%{__rm} -f %{buildroot}%{_sysconfdir}/ganglia/conf.d/modgstatus.conf
# Clean up the .conf.in files
%{__rm} -f %{buildroot}%{_sysconfdir}/ganglia/conf.d/*.conf.in
## Disable the diskusage module until it is configured properly
#mv %{buildroot}%{_sysconfdir}/ganglia/conf.d/diskusage.pyconf %{buildroot}%{_sysconfdir}/ganglia/conf.d/diskusage.pyconf.off
# Don't install Makefile* in the web dir
%{__rm} -f %{buildroot}%{_datadir}/ganglia/Makefile*

## Install binaries
%{__make} install DESTDIR="%{buildroot}"
## House cleaning
%{__rm} -f ${buildroot}%{_datadir}/ganglia/{Makefile.am,version.php.in}

%clean
%{__rm} -rf %{buildroot}

%pre
## Add the "ganglia" user
/usr/sbin/useradd -c "Ganglia Monitoring System" \
        -s /sbin/nologin -r -d %{_localstatedir}/lib/ganglia ganglia 2> /dev/null || :
/sbin/ldconfig

%post -p /sbin/ldconfig

%post gmond
/sbin/chkconfig --add gmond

%post gmetad
/sbin/chkconfig --add gmetad

%preun gmetad
if (( $1 == 0 )); then
    /sbin/service gmetad stop &>/dev/null || :
    /sbin/chkconfig --del gmetad
fi

%preun gmond
if (( $1 == 0 )); then
    /sbin/service gmond stop &>/dev/null || :
    /sbin/chkconfig --del gmond
fi

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/ganglia-config
%dir %{_libdir}/ganglia/
%{_libdir}/ganglia/*.so
%{_libdir}/libganglia*.so.*
%exclude %{_libdir}/ganglia/modpython.so

%files gmetad
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/gmetad.1*
%config %{_sysconfdir}/init.d/gmetad
%dir %{_sysconfdir}/ganglia/
%config(noreplace) %{_sysconfdir}/ganglia/gmetad.conf
%{_sbindir}/gmetad
%dir %{_localstatedir}/lib/ganglia/
%defattr(0755, ganglia, ganglia)
%{_localstatedir}/lib/ganglia/rrds/

%files gmond
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/gmetric.1*
%doc %{_mandir}/man5/gmond.conf.5*
%doc %{_mandir}/man1/gmond.1*
%doc %{_mandir}/man1/gstat.1*
%config %{_sysconfdir}/init.d/gmond
%dir %{_sysconfdir}/ganglia/
%dir %{_sysconfdir}/ganglia/conf.d/
%config(noreplace) %{_sysconfdir}/ganglia/gmond.conf
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/*.conf
%{_bindir}/gmetric
%{_bindir}/gstat
%{_sbindir}/gmond
%exclude %{_sysconfdir}/ganglia/conf.d/modpython.conf

%files gmond-python
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/*.pyconf*
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/modpython.conf
%dir %{_libdir}/ganglia/python_modules/
%{_libdir}/ganglia/python_modules/*.py*
%{_libdir}/ganglia/modpython.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/libganglia*.so
%exclude %{_libdir}/libganglia*.la

%files web
%defattr(-, root, root, 0755)
%doc web/AUTHORS web/COPYING
%config(noreplace) %{_sysconfdir}/ganglia/conf.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ganglia.conf
%{_datadir}/ganglia/

%defattr(0640, root, apache)
%config(noreplace) %{_sysconfdir}/ganglia/private_clusters/

%changelog
* Mon Jan 30 2012 David Hrbáč <david@hrbac.cz> - 3.1.7-3
- intial rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 3.1.7-2
- Rebuild for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Apr 22 2010 Kostas Georgiou <georgiou@fedoraproject.org> - 3.1.7-1
- New upstream release
- Spec file cleanups
- Use the new name_match feature to enable the diskusage plugin by default

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 29 2009 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 3.1.2-3
- Rebuilt for #492703, no obvious reasons why the previous build was bad :(

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 3.1.2-1
- Update to 3.1.2
- Remove unneeded patch for CVE-2009-0241

* Tue Jan 20 2009 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 3.1.1-4
- [480236] Updated patch for the buffer overflow from upstream with
  additional fixes

* Wed Jan 14 2009 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 3.1.1-3
- Fix for gmetad server buffer overflow
- The private_clusters file should not be readable by everyone

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.1.1-2
- Rebuild for Python 2.6

* Fri Oct 24 2008 Jarod Wilson <jarod@redhat.com> 3.1.1-1
- Update to 3.1.1

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> 3.1.0-2
- Include unowned directories.

* Mon Aug 11 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> 3.1.0-1
- Upstream patches from 3.1.1
- Move private_clusters config to /etc and mark it as a config file
- Only allow connections from localhost by default on the web frontend
- Add some extra module config files (modules are always loaded at the
  moment so removing the configs has no effect beyond metric collection
  (upstream is working on way way to disable module loading from the
  configs)

* Tue Jul 29 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> 3.1.0-0.5
- Add the config files for the python module

* Thu Jul 17 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> 3.1.0-0.4
- Update to the 3.1.0 pre-release
- Fixes gmond.conf to use the ganglia user and not nobody
- Removal of the ppc64 work-around
 
* Fri Jun 13 2008 Jarod Wilson <jwilson@redhat.com> 3.1.0-0.3.r1399
- One more try at work-around. Needs powerpc64, not ppc64...

* Fri Jun 13 2008 Jarod Wilson <jwilson@redhat.com> 3.1.0-0.2.r1399
- Work-around for incorrectly hard-coded libdir on ppc64

* Wed Jun 11 2008 Jarod Wilson <jwilson@redhat.com> 3.1.0-0.1.r1399
- Update to 3.1.x pre-release snapshot, svn rev 1399

* Mon Jun 09 2008 Jarod Wilson <jwilson@redhat.com> 3.0.7-2
- Bump and rebuild against latest rrdtool

* Wed Feb 27 2008 Jarod Wilson <jwilson@redhat.com> 3.0.7-1
- New upstream release
- Fixes "Show Hosts" toggle
- Fixes to host view metric graphs
- Fixes two memory leaks

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> 3.0.6-2
- Bump and rebuild with gcc 4.3

* Mon Dec 17 2007 Jarod Wilson <jwilson@redhat.com> 3.0.6-1
- New upstream release (security fix for web frontend
  cross-scripting vulnerability) {CVE-2007-6465}

* Wed Oct 24 2007 Jarod Wilson <jwilson@redhat.com> 3.0.5-2
- Reorg packages to fix multilib conflicts (#341201)

* Wed Oct 03 2007 Jarod Wilson <jwilson@redhat.com> 3.0.5-1
- New upstream release

* Fri May 18 2007 Jarod Wilson <jwilson@redhat.com> 3.0.4-3
- Add missing Req: php-gd so people will see nifty pie charts

* Sat Mar 24 2007 Jarod Wilson <jwilson@redhat.com> 3.0.4-2
- Own created directories (#233790)

* Tue Jan 02 2007 Jarod Wilson <jwilson@redhat.com> 3.0.4-1
- New upstream release

* Thu Nov 09 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-11
- gmond also needs ganglia user (#214762)

* Tue Sep 05 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-10
- Rebuild for new glibc

* Fri Jul 28 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-9
- Add missing Reqs on chkconfig and service
- Make %%preun sections match Fedora Extras standards
- Minor %%configure tweak

* Tue Jul 11 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-8
- Add missing php req for ganglia-web
- Misc tiny spec cleanups

* Tue Jun 13 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-7
- Clean up documentation

* Mon Jun 12 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-6
- Remove misplaced execute perms on source files

* Thu Jun 08 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-5
- Whack Obsoletes/Provides, since its never been in FE before
- Use mandir macro
- Check if service is running before issuing a stop in postun
- Remove shadow-utils Prereq, its on the FE exception list

* Mon Jun 05 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-4
- Run things as user ganglia instead of nobody
- Don't turn on daemons by default

* Mon Jun 05 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-3
- Kill off static libs
- Add URL for Source0

* Mon Jun 05 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-2
- Move web-frontend from /var/www/html/ to /usr/share/
- Make everything arch-specific

* Thu Jun 01 2006 Jarod Wilson <jwilson@redhat.com> 3.0.3-1
- Initial build for Fedora Extras, converting existing spec to
  (attempt to) conform with Fedora packaging guidelines
