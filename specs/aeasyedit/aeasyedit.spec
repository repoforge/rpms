# $Id$
# Authority: shuff
# Upstream: Hugh Mahon <hugh$mahon,cwx,net>

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define real_name aee

Name:         aeasyedit
Summary:      Another Easy Text Editor
Version:      2.2.15b
Release:      1%{?dist}
License:      Artistic
Group:        Applications/Editors
URL:          http://mahon.cwx.net/

Source:      http://mahon.cwx.net/sources/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make
BuildRequires: glibc-devel
BuildRequires: ncurses-devel
%{!?_without_modxorg:BuildRequires: libX11-devel, libXau-devel, libxcb-devel, libXdmcp-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Requires: glibc
Requires: ncurses
Requires: libXau, libxcb, libXdmcp

Provides: aee, rae
Provides: xae, rxae

%description
EE is a an easy to use text editor. Intended to be usable with little or no
instruction. Provides both a terminal (curses based) interface and native
X-Windows interface (in which case the executable is called xae). Features
include pop-up menus, journalling (to recover from system crash or loss of
connection), cut-and-paste, multiple buffers (associated with files or not),
and much more. 

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} both
 

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%{__install} -m 0755 aee %{buildroot}%{_bindir}/aee
%{__install} -m 0755 xae %{buildroot}%{_bindir}/xae
pushd %{buildroot}%{_bindir}
%{__ln_s} aee rae
%{__ln_s} xae rxae
popd
%{__install} -m 0644 aee.1 %{buildroot}%{_mandir}/man1/aee.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(755,root,root,-)
%doc %{_mandir}/man?/*
%{_bindir}/*


%changelog
* Mon Nov 02 2009 Steve Huff <shuff@vecna.org> - 2.2.15b-1
- Initial package.
