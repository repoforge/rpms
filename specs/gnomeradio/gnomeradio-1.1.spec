# $Id$
# Authority: dag
# ExclusiveDist: rh7

Summary: FM-Tuner program for GNOME
Name: gnomeradio
Version: 1.1
Release: 0%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mfcn.ilo.de/gnomeradio

Source: http://mfcn.ilo.de/gnomeradio/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: pkgconfig, intltool

%description
A FM-Tuner program for GNOME.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/apps/Multimedia/*.desktop

%changelog
* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> 1.1-0
- Initial package. (using DAR)
