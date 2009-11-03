# $Id$

# Authority: dag

### FIXME: Makefile uses gcc hardcoded
# Distcc: 0
#
### FIXME: Makefile creates symlinks to outside buildroot
# Soapbox: 0

%define real_name Gemu

Summary: GNOME EMU10K1 configuration tool
Name: gemu
Version: 0.8
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.roadfeldt.com/

Source0: http://dl.sf.net/gemu/gemu-%{version}.tar.gz
Source1: http://dl.sf.net/emu10k1/emu10k1-v0.20a.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
The purpose of Gemu is to control sound cards based on the EMU10K1
platform. It is meant to allow control to all aspects of EMU10K1 based
sound cards. Features include route creation, effect/patch control, misc.
card settings, route volume mixer, source and destination mixers, and OSS
Mixer binding.

%prep
%setup -n %{real_name}-%{version} -a 1
#%setup -n %{real_name}-%{version}

%build
(cd emu10k1-v0.20a; %{__make}; %{__make} tools)
#cd emu10k1-v0.20a
#%{__make}
#%{__make} tools
#cd -
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/gemu
%{_datadir}/gnome/apps/Multimedia/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-0.2
- Rebuild for Fedora Core 5.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
