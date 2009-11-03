# $Id$
# Authority: dag

# Distcc: 0

Summary: Tools for configuring and controlling emu10k1 based soundcards
Name: emu-tools
Version: 0.9.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://opensource.creative.com/

Source: http://dl.sf.net/emu10k1/emu-tools-%{version}.tar.gz
Patch0: emu-tools-0.9.4-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The emu-tools are used to control emu10k1 based (SBLive) and
Audigy based soundcards from Creative Labs.

The emu-config program is used to configure such things as output
speaker mode (digital/analog), spdif sample rate, etc.

The emu-dspmgr program is used to control how signals are routed inside
the emu10k1 and Audigy chips. It can also be used to load effects, add
volume controls and much more.

The emu-tools currently are intended for use with kernel's 2.4.12 or higher.
They will not work with the Alsa driver.

%prep
%setup
%patch0 -b .gcc33

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	man_prefix="%{buildroot}%{_mandir}" \
	script_dir="%{buildroot}%{_sysconfdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc GNU_GPL docs/*
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/emu10k1/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Added %%{optflags} buildflags.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.9.4-0
- Initial package. (using DAR)
