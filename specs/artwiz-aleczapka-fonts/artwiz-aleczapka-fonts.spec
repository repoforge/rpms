# $Id$
# Authority: dag


%{!?dtag:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el4:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%define fontdir %{_datadir}/fonts/artwiz-aleczapka

Summary: Set of (improved) artwiz fonts
%define real_name artwiz-aleczapka-en-sources
Name: artwiz-aleczapka-fonts
Version: 1.3
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://artwizaleczapka.sourceforge.net/

Source: http://dl.sf.net/artwizaleczapka/artwiz-aleczapka-en-sources-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{?_with_modxorg:BuildRequires: xorg-x11-font-utils}
%{!?_with_modxorg:BuildRequires: XFree86}

%description
artwiz-aleczapka-fonts is set of (improved) artwiz fonts.

%prep
%setup -n %{real_name}-%{version}

%build
sh makepcf.sh

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{fontdir}/artwiz-aleczapka/
%{__install} -p -m0644 *.pcf %{buildroot}%{fontdir}/artwiz-aleczapka/

touch %{buildroot}%{fontdir}/artwiz-aleczapka/fonts.cache-{1,2}

%clean
%{__rm} -rf %{buildroot}

%post
%{_bindir}/fc-cache -f %{_datadir}/fonts/artwiz-aleczapka/ || :

%postun
if [ $1 -eq 0 ]; then
        %{_bindir}/fc-cache -f %{_datadir}/fonts/artwiz-aleczapka/ || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README VERSION
%dir %{fontdir}/artwiz-aleczapka/
%{fontdir}/artwiz-aleczapka/*.pcf
%ghost %{fontdir}/artwiz-aleczapka/fonts.cache-1
%ghost %{fontdir}/artwiz-aleczapka/fonts.cache-2

%changelog
* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
