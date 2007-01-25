# $Id$
# Authority: dag

Summary: Multi-purpose WAVE data processing and reporting utility
Name: shntool
Version: 3.0.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.etree.org/shnutils/shntool/

Source: http://www.etree.org/shnutils/shntool/source/shntool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: shorten, flac, sox
Requires: shorten, flac, sox

%description
shntool is a multi-purpose WAVE data processing and reporting
utility. File formats are abstracted from its core, so it can process
any file that contains WAVE data, compressed or not - provided there
exists a format module to handle that particular file type.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Thu Jan 25 2007 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1.

* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Initial package. (using DAR)
