# Authority: dag

Summary: VCR is a program which enables you to record a program using a video grabber card
Name: vcr
Version: 1.09
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://www.stack.nl/~brama/vcr/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.stack.nl/~brama/vcr/src/%{name}-%{version}.tar.gz
Patch: %{name}-1.09-avifile.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: avifile-devel
Requires: avifile

%description
VCR is a program which enables you to record a program using a video 
grabber card that's supported by the video4linux drivers. It doesn't 
require a graphical environment, and you can use all popupular windows 
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the 
avifile library. Now, you can finally record your favourite program from a 
remote place, because Murphy's law dictates that you remember to record it 
when you're as far away from your home as possible...

%prep
%setup
%patch0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/vcr/*

%changelog
* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 1.09
- Added avifile0.7 patch to get it to build.

* Fri May 30 2002 Dag Wieers <dag@wieers.com> - 1.07
- Initial package.
