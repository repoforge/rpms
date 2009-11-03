# $Id$
# Authority: dag

%define python_minver 2.3.4

%define zope_home      %{_libdir}/zope
%define software_home  %{zope_home}/lib/python
%define instance_home  %{_localstatedir}/lib/zope

%define zopectl        %{_bindir}/zopectl
%define runzope        %{_bindir}/runzope

Summary: Web application server for flexible content management applications
Name: zope
Version: 2.8.7
Release: 1%{?dist}
License: ZPL
Group: System Environment/Daemons
URL: http://www.zope.org/

Source0: http://zope.org/Products/Zope/%{version}/Zope-%{version}-final.tgz
Source1: zope.init.in
Source2: zope.sysconfig.in
Source3: zope.zopectl.in
Source4: zope-README.Fedora
Source5: zope.logrotate.in
Source6: zope.logrotate.cron.in
Source10: http://www.zope.org/Products/Zope/Hotfix-2006-07-05/Hotfix-20060705/Hotfix_20060705.tar.gz
Patch0: zope-2.7.3-config.patch
Patch1: zope-2.8.3-pythonwarning.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= %{python_minver} 
BuildRequires: python >= %{python_minver} 
Requires: python >= %{python_minver}

Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service

%description
Zope is an application server framework that enables developers to quickly
build web applications such as intranets, portals, and content management
systems.

After starting Zope, you can access it by pointing your browser to
http://localhost:8080

WARNING: this zope package has been built on python 2.4.X, which is not
supported ! Do not file bugreports or ask for support on zope.org if you
choose to use this package.


%prep
%setup -n Zope-%{version}-final
%patch0 -p1 -b .config
# remove the backup, or we'll install it too...
rm -f skel/etc/zope.conf.in.config skel/lib/python/README.txt.in
# Warning on the default index_html about python 2.4 & zope 2.8
%patch1 -p1 -b .pythonwarning

%{__chmod} -x skel/import/README.txt
%{__install} -p -m0644 %{SOURCE4} README.Fedora
%{__install} -p -m0644 %{SOURCE5} skel/etc/logrotate.conf.in


%build
./configure \
  --with-python="%{__python}" \
  --prefix="%{buildroot}%{zope_home}" \
  --optimize
  
#    --no-compile

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__rm} -f docs

# Create all required additional directories
for dir in %{zope_home} %{software_home} %{instance_home}/{Products,bin,var} \
    %{_sysconfdir}/sysconfig %{_bindir}; do
    mkdir -p %{buildroot}$dir
done


%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/zope
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/zope
%{__install} -Dp -m0755 %{SOURCE3} %{buildroot}%{_bindir}/zopectl
%{__install} -Dp -m0755 %{SOURCE6} %{buildroot}%{_sysconfdir}/cron.daily/zope-logrotate
%{__perl} -pi -e 's|<<SYSCONFDIR>>|%{_sysconfdir}|g;
             s|<<BINDIR>>|%{_bindir}|g;
             s|<<LOCALSTATEDIR>>|%{_localstatedir}|g;
             s|<<ZOPE_USER>>|zope|g' \
    %{buildroot}%{_initrddir}/zope \
    %{buildroot}%{_sysconfdir}/sysconfig/zope \
    %{buildroot}%{_bindir}/zopectl \
    %{buildroot}%{_sysconfdir}/cron.daily/zope-logrotate \
    README.Fedora skel/etc/zope.conf.in

# Install the skel, translating paths, into the build root
%{__python} "utilities/copyzopeskel.py" \
     --sourcedir="skel" \
     --targetdir="%{buildroot}%{instance_home}" \
     --replace="INSTANCE_HOME:%{instance_home}" \
     --replace="SOFTWARE_HOME:%{software_home}" \
     --replace="ZOPE_HOME:%{zope_home}" \
     --replace="PYTHON:%{__python}" \

# Actually copy all the other files over
%{__make} install

# Hotfix
tar -xzf %{SOURCE10} -C %{buildroot}%{software_home}/Products

%{__chmod} 700 %{buildroot}%{instance_home}
%{__chmod} 755 %{buildroot}%{zope_home}

# Symlink to include in the docs
%{__ln_s} -f %{zope_home}/doc docs

# write version.txt
echo "Zope %{version}-%{release}" > \
    "%{buildroot}%{software_home}/version.txt"

# Compile .pyc
%{__python} -c "import compileall; \
    compileall.compile_dir(\"%{buildroot}%{zope_home}\", \
    ddir=\"%{zope_home}\", force=1)"

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -c "Zope user" -s /bin/false -r -d %{zope_home} zope 2>/dev/null || :

%post
# add zope init to runlevels
/sbin/chkconfig --add zope

%preun
if [ $1 -eq 0 ]; then
  /sbin/service zope stop >/dev/null 2>&1
  /sbin/chkconfig --del zope
fi

%files 
%defattr(-, root, root, 0775)
%doc %{zope_home}/doc/
%doc README.Fedora docs
%config(noreplace) %{_sysconfdir}/sysconfig/zope
%config %{_initrddir}/zope
%config %{_sysconfdir}/cron.daily/zope-logrotate
%dir %{zope_home}
%{zope_home}/bin/
%{zope_home}/import/
%{zope_home}/lib/

%dir %{zope_home}/skel/
%config %{zope_home}/skel/etc/
%{zope_home}/skel/bin/
%{zope_home}/skel/Extensions/
%{zope_home}/skel/import/
%{zope_home}/skel/log/
%{zope_home}/skel/Products/
%{zope_home}/skel/README.txt
%{zope_home}/skel/var/

%defattr(0755, root, root)
%{_bindir}/zopectl

%defattr(-, zope, zope, 0755)
%dir %{instance_home}
%config %{instance_home}/etc/
%{instance_home}/bin/
%{instance_home}/Extensions/
%{instance_home}/import/
%{instance_home}/log/
%{instance_home}/Products/
%{instance_home}/README.txt
%{instance_home}/var/

%changelog
* Thu Nov 09 2006 Dag Wieers <dag@wieers.com> - 2.8.7-1
- Updated to release 2.8.7.

* Wed Aug  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.8.3-5
- Security: fix world-writable permissions on logrotate config files
  and README.Fedora (#200794).

* Mon Jul 10 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.8.3-4
- add Hotfix_20060705

* Tue Oct 25 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.3-3
- rebuild

* Tue Oct 25 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.3-2
- add warning about zope 2.8 & python 2.4 (bug 171681)

* Sat Oct 22 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.3-1
- version 2.8.3

* Sat Oct 15 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.2-1
- version 2.8.2

* Sat Sep 10 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.1-1
- version 2.8.1

* Sun Jun 12 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.0-2
- rebuild

* Sat Jun 11 2005 Aurelien Bompard <gauret[AT]free.fr> 2.8.0-1
- version 2.8.0

* Sun Jun 05 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7.6-2
- don't remove the zope user un postun (to keep the Data.fs to the
  correct owner after removal)

* Sun May 08 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7.6-1%{?dist}
- version 2.7.6
- use disttag

* Thu Apr 07 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7.5-2.fc4
- add hotfix

* Thu Mar 24 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7.5-1.fc4
- version 2.7.5
- drop Epoch
- change release tag for FC4
- convert some tabs into spaces

* Wed Jan 26 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7.4-1
- version 2.7.4
- flag the documentation as %%doc
- make %%zope_home go+rx to allow users to create instances and to allow
  access to docs
- add a logrotate cron job
- flag config files as %%config even in %%zope_home and %%instance_home

* Fri Dec 10 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.6
- activate "security-policy-implementation python" in zope.conf

* Sun Nov 21 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.5
- revert to zope's default directory tree to allow multiple instances
- make the zopectl script multiple-instaces-aware.
- add README.Fedora

* Fri Nov 12 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.4
- compile scripts in %zope_home/bin too
- keep skel dir in %zope_home to fix mkzopeinstance
- BuildRequire python, since python-devel doesn't require it.

* Fri Nov 12 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.3
- compile .pyc instead of just touch-ing them

* Thu Nov 11 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.2
- deal with leftover .pyc files
- minor spec cleanups

* Thu Nov 11 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.3-0.fdr.1
- fix scriptlets requirements
- use standard buildroot
- replace %%buildroot by RPM_BUILD_ROOT
- update to 2.7.3
- drop Hotfix
- drop patch 1, fixed upstream

* Tue Aug 10 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.2-0.fdr.3
- add hotfix from Zope.org: 
  http://zope.org/Products/Zope/Hotfix-200400807/Hotfix-20040807-alert

* Wed Aug 04 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.2-0.fdr.2
- add patch to warn the user that the initial user cannot be added while
  Zope is running (from Chris McDonough)

* Wed Aug 04 2004 Aurelien Bompard <gauret[AT]free.fr> 2.7.2-0.fdr.1
- version 2.7.2
- remove leftover byte-compilation in %%post
- Zope 2.7.x really requires python >= 2.3.3

* Wed Jul 14 2004 Rex Dieter <rexdieter at sf.net> 2.7.1-0.fdr.1
- 2.7.1
- move files created in %%post back into rpm.  Unowned files are bad.
- make (theoretically) buildable for all rh73-rh90,fc1/2,el3
  NOTE: lowerred python_minver to 2.2.2 to test builds, though (most) 
  docs claim 2.3.3 is required.  (??) 
- don't use Requires(preun,postun)
- use %%_smp_mflags

* Tue Apr 28 2004 Chris McDonough <chrism@plope.com> 2.7.0-0.fdr.1
- Prep for submission to Fedora.us by revising work done by Matthias
- Refer to source files by URL instead of by name
- Write version.txt into software home in post
- Don't ship byte-compiled files, instead compile them in post
- Add patch for inverted P_WAIT/P_NOWAIT in zdctl (fixes startup)
- Add patch for objectmanager bug that could effect sites that depend
  on userid/username separation
- Improved init script (OK and FAILED now are printed at the appropriate
  times)
- Remove runzope workaround by adding a <zoperunner> stanza to the
  config file.
- Start in runlevels 345.
- Known issues:
  - zopectl is started and runs as the root user at boot time,
    (although Zope itself runs as the zope user)
  - no distro-specific docs telling people which port the software
    runs on or how to add a user via zopectl adduser.

* Wed Feb 18 2004 Matthias Saou <http://freshrpms.net/> 2.7.0-0.6.fr
- Initial RPM release.
- The startup/stop needs to be modified further.
- Currently "zopectl" returns an error although Zope does start...

