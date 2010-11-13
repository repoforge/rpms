# $Id$
# Authority: dag

Summary: RPM macros used by the RPMForge project
Name: rpm-macros-rpmforge
Version: 0
Release: 5%{?dist}
License: GPL
Group: Development/Tools
URL: http://rpmforge.net/

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPM macros used by the RPMForge project.

%prep

%{__cat} <<EOF >macros.rpmforge
### RPM macros for RPMForge project (http://rpmforge.net/)
###
### Add to /etc/rpmrc: "macrofiles: /etc/rpm/macros.rpmforge"

#%%packager RPMForge authority <%%{name}@package.rpmforge.net>
#%%vendor RPMForge project (http://rpmforge.net/)

%if %{?dtag:1}0
%%{!?dtag:%%dtag %dtag}
%%{!?%dtag:%%%dtag 1}
%%{!?dist:%%dist .%dtag}
%endif
%if "%dtag" == "el6"
%%distribution RPMForge repository for Red Hat Enterprise Linux 6
%%errata 106
%endif
%if "%dtag" == "el5"
%%distribution RPMForge repository for Red Hat Enterprise Linux 5
%%errata 105
%endif
%if "%dtag" == "el4"
%%distribution RPMForge repository for Red Hat Enterprise Linux 4
%%errata 104
%endif
%if "%dtag" == "el3"
%%distribution RPMForge repository for Red Hat Enterprise Linux 3
%%errata 103
%endif
%if "%dtag" == "rh9"
%%distribution RPMForge repository for Red Hat Linux 9
%%errata 90
%endif
%if "%dtag" == "rh7"
%%distribution RPMForge repository for Red Hat Linux 7.X
%%errata 73
%endif
%if "%dtag" == "el2"
%%distribution RPMForge repository for Red Hat Enterprise Linux 2.1
%%errata 72
%endif

#==============================================================================
# ---- Generic auto req/prov filtering macros
#
# http://fedoraproject.org/wiki/PackagingDrafts/AutoProvidesAndRequiresFiltering

# prevent anything matching from being scanned for provides
%%filter_provides_in(P) %%{expand: \\
%%global __filter_prov_cmd %%{?__filter_prov_cmd} %%{__grep} -v %%{-P} '%%*' | \\
}

# prevent anything matching from being scanned for requires
%%filter_requires_in(P) %%{expand: \\
%%global __filter_req_cmd %%{?__filter_req_cmd} %%{__grep} -v %%{-P} '%%*' | \\
}

# filter anything matching out of the provides stream
%%filter_from_provides() %%{expand: \\
%%global __filter_from_prov %%{?__filter_from_prov} | %%{__sed} -e '%%*' \\
}

# filter anything matching out of the requires stream
%%filter_from_requires() %%{expand: \\
%%global __filter_from_req %%{?__filter_from_req} | %%{__sed} -e '%%*' \\
}

# actually set up the filtering bits 
%%filter_setup %%{expand: \\
%%global _use_internal_dependency_generator 0 \\
%%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%%{1} \${FILE}; done | /bin/sort -u \\
%%global __find_provides /bin/sh -c "%%{?__filter_prov_cmd} %%{__deploop P} %%{?__filter_from_prov}" \\
%%global __find_requires /bin/sh -c "%%{?__filter_req_cmd}  %%{__deploop R} %%{?__filter_from_req}" \\
}
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 macros.rpmforge %{buildroot}%{_sysconfdir}/rpm/macros.rpmforge

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/rpm/macros.rpmforge

%changelog
* Thu Nov 11 2010 Dag Wieers <dag@wieers.com> - 0-5
- Added EL6 support.

* Tue Nov 03 2009 Dag Wieers <dag@wieers.com> - 0-4
- Added default %%dist when unset.
- Added %%distribution and %%errata for RHEL4 and RHEL5.

* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 0-3
- Add __find_provides/__find_requires filter macros from fedora.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0-1
- Initial package. (using DAR)
