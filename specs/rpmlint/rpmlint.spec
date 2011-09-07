# $Id$
# Authority: yury
# Upstream: rpmlint-discuss$zarb,org
#
# Thank you upstream for shipping xz-only tarballs!
# Also, python-magic / python-enchant are RHEL6-only.
#
# ExclusiveDist: el6
#
### EL6 ships with rpmlint-0.94-2
# Tag: rfx
#

Summary: Tool for checking common errors in RPM packages
Name: rpmlint
Version: 1.3
Release: 1%{?dist}
License: GPLv2
Group: Development/Tools
URL: http://rpmlint.zarb.org/

Source0: http://rpmlint.zarb.org/download/%{name}-%{version}.tar.xz
Source1: %{name}.config
Source3: %{name}-etc.config
# EL-4 specific config
Source4: %{name}.config.el4
# EL-5 specific config
Source5: %{name}.config.el5

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python >= 2.4
BuildRequires: rpm-python >= 4.4
BuildRequires: sed >= 3.95

Requires: python >= 2.4
Requires: rpm-python >= 4.4

Requires: python-magic
Requires: python-enchant

Requires: cpio
Requires: binutils
Requires: desktop-file-utils
Requires: gzip
Requires: bzip2
Requires: xz

%description
rpmlint is a tool for checking common errors in RPM packages.  Binary
and source packages as well as spec files can be checked.

%prep
%setup
sed -i -e /MenuCheck/d Config.py
cp -p config config.example
install -pm 644 %{SOURCE3} config

%build
%{__make} %{?_smp_mflags} COMPILE_PYC=1

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=$RPM_BUILD_ROOT ETCDIR=%{_sysconfdir} MANDIR=%{_mandir} \
  LIBDIR=%{_datadir}/rpmlint BINDIR=%{_bindir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/rpmlint/config

install -pm 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/rpmlint/config.el4
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/rpmlint/config.el5
pushd $RPM_BUILD_ROOT%{_bindir}
ln -s rpmlint el4-rpmlint
ln -s rpmlint el5-rpmlint
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* config.example
%config(noreplace) %{_sysconfdir}/rpmlint/
%{_sysconfdir}/bash_completion.d/rpmlint
%{_bindir}/rpmdiff
%{_bindir}/el*-rpmlint
%{_bindir}/rpmlint
%{_datadir}/rpmlint/
%{_mandir}/man1/rpmlint.1*

%changelog
* Wed Sep 07 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3-1
- Synced the SPEC with the latest version from Fedora Rawhide.
- Updated to release 1.3.

* Mon Jan 04 2010 Bjarne Saltbaek <arnebjarne72@hotmail.com> - 0.92-1
- Updated to release 0.92.
- Added COMPILE_PYC=1 for *.pyc compilation.
- Python >= 2.4 now required.

* Wed Sep  1 2004 Matthias Saou <http://freshrpms.net/> 0.61-0
- Update to 0.61.
- Include an updated default configuration suitable for Red Hat Linux and
  Fedora Core made from scratch today.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.51-0
- Updated to release 0.51.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.46-0
- Initial package. (using DAR)

