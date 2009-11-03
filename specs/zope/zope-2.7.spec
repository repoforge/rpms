# $Id$
# Authority: matthias

%define real_name      Zope
%define real_version   2.7.2-0
%define python         %{_bindir}/python
%define python_minver  2.3.3
%define zope_user      zope
%define zope_group     zope

%define zope_home      %{_prefix}/lib/zope
%define software_home  %{zope_home}/lib/python
%define instance_home  %{_var}/lib/zope
%define client_home    %{instance_home}/data
%define run_dir        %{_var}/run/zope
%define log_dir        %{_var}/log/zope
%define config_file    %{_sysconfdir}/zope.conf

%define zopectl        %{_bindir}/zopectl
%define runzope        %{_bindir}/runzope


Summary: Web application server for flexible content management applications
Name: zope
Version: 2.7.2
Release: 0.1%{?dist}
License: ZPL
Group: System Environment/Daemons
URL: http://www.zope.org/
Source0: http://zope.org/Products/Zope/%{version}/%{real_name}-%{real_version}.tgz
Source1: zope.init.in
Source2: zope.logrotate.in
Patch: Zope-2.7.0-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python >= %{python_minver}
Requires(pre): /usr/sbin/useradd
Requires(post): /usr/sbin/userdel
Requires(preun,postun): /sbin/chkconfig, /sbin/service
BuildRequires: python >= %{python_minver}, python-devel >= %{python_minver}

%description
Zope is an open source application server for building content managements,
intranets, portals, and custom applications. The Zope community consists of
hundreds of companies and thousands of developers all over the world, working
on building the platform and Zope applications. Zope is written in Python, a
highly-productive, object-oriented scripting language.


%prep
%setup -n %{real_name}-%{version}-0
%patch -p1 -b .config


%build
./configure \
    --with-python=%{python} \
    --prefix=%{buildroot}%{zope_home} \
    --optimize
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} rpm-skel

# Copy over files from the default skel to the rpm-skel
%{__install} -Dp -m 644 skel/etc/zope.conf.in rpm-skel/etc/zope.conf.in
%{__install} -Dp -m 755 skel/bin/runzope.in rpm-skel%{_bindir}/runzope.in
%{__install} -Dp -m 755 skel/bin/zopectl.in rpm-skel%{_bindir}/zopectl.in

# Create all required additional directories
for dir in %{zope_home} %{software_home} %{client_home} %{log_dir} %{run_dir} \
    %{instance_home}/{Products,bin}; do
        %{__mkdir_p} %{buildroot}$dir
done

# Install additional files in the rpm-skel
%{__install} -Dp -m 755 %{SOURCE1} rpm-skel%{_sysconfdir}/rc.d/init.d/zope.in
%{__install} -Dp -m 644 %{SOURCE2} rpm-skel%{_sysconfdir}/logrotate.d/zope.in

# Install the skel, translating paths, into the build root
%{python} "utilities/copyzopeskel.py" \
     --sourcedir="rpm-skel" \
     --targetdir="%{buildroot}" \
     --replace="INSTANCE_HOME:%{instance_home}" \
     --replace="CLIENT_HOME:%{client_home}" \
     --replace="RUN_DIR:%{run_dir}" \
     --replace="LOG_DIR:%{log_dir}" \
     --replace="SOFTWARE_HOME:%{software_home}" \
     --replace="ZOPE_HOME:%{zope_home}" \
     --replace="ZOPE_USER:%{zope_user}" \
     --replace="CONFIG_FILE:%{config_file}" \
     --replace="PYTHON:%{python}" \
     --replace="ZOPECTL:%{zopectl}" \
     --replace="RUNZOPE:%{runzope}"

# Now, copy all the other files over
%{__make} install

# Symlink to include in the docs
%{__ln_s} %{zope_home}/doc docs

# Workaround
%{__ln_s} %{runzope} %{buildroot}%{instance_home}/bin/


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -c "Zope user" -s /bin/false -r -d %{zope_home} \
    %{zope_user} 2>/dev/null || :


%post
/sbin/chkconfig --add zope


%preun
if [ $1 -eq 0 ]; then
    /sbin/service zope stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del zope
fi


%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel %{zope_user} 2>/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc docs
%config(noreplace) %{config_file}
%config(noreplace) %{_sysconfdir}/logrotate.d/zope
%config %{_sysconfdir}/rc.d/init.d/zope
%attr(0755, root, root) %{runzope}
%attr(0755, root, root) %{zopectl}
%dir %{zope_home}/
%{zope_home}/bin/
%{zope_home}/doc/
%{zope_home}/import/
%{zope_home}/lib/
%exclude %{zope_home}/skel/
%attr(0700, %{zope_user}, %{zope_group}) %verify(not md5 size mtime) %{instance_home}/
%attr(0755, %{zope_user}, %{zope_group}) %dir %{_var}/log/zope/
%attr(0755, %{zope_user}, %{zope_group}) %dir %{_var}/run/zope/


%changelog
* Wed Oct 20 2004 Matthias Saou <http://freshrpms.net/> 2.7.2-0.1
- Update to 2.7.2.
- Minor spec updates and cleanups.

* Wed Jul 14 2004 Matthias Saou <http://freshrpms.net/> 2.7.1-0.1
- Update to 2.7.1.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 2.7.0-0.7
- SVN import, minor tweaks.

* Wed Feb 18 2004 Matthias Saou <http://freshrpms.net/> 2.7.0-0.6
- Initial RPM release.
- The startup/stop needs to be modified further.
- Currently "zopectl" returns an error although Zope does start...

