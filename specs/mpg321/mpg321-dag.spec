# Authority: freshrpms
# Dists: rh80 rh90

Summary: MPEG audio player
Name: mpg321
Version: 0.2.10
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mpg321.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/mpg321/mpg321-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libao-devel >= 0.8.0, libmad >= 0.14.2b
Obsoletes: mpg123

%description
mpg321 is a Free replacement for mpg123, a very popular command-line mp3
player. mpg123 is used for frontends, as an mp3 player and as an mp3 to
wave file decoder (primarily for use with CD-recording software.) In all 
of these capacities, mpg321 can be used as a drop-in replacement for
mpg123.

%prep
%setup

%build
%configure --with-default-audio="esd"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING HACKING NEWS README* THANKS TODO
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 0.2.10-0
- Initial package. (using DAR)
