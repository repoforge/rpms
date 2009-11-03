# $Id$
# Authority: dag

Summary: Graphical frontend for subversion
Name: esvn
Version: 0.6.12
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://esvn.umputun.com/

Source: http://dl.sf.net/esvn/esvn-%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, subversion-devel, gcc-c++
Requires: qt-devel, qt, subversion

%description
eSvn is a graphical frontend for the subversion revision system.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 esvn %{buildroot}%{_bindir}/esvn
%{__install} -Dp -m0755 esvn-diff-wrapper %{buildroot}%{_bindir}/esvn-diff-wrapper
%{__install} -Dp -m0644 esvn.png %{buildroot}%{_datadir}/pixmaps/esvn.png
%{__install} -Dp -m0644 eSvn.desktop %{buildroot}%{_datadir}/applications/esvn.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENSE README html-docs/*
%{_bindir}/esvn
%{_bindir}/esvn-diff-wrapper
%{_datadir}/pixmaps/esvn.png
%{_datadir}/applications/esvn.desktop

%changelog
* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 0.6.12-1
- Update to release 0.6.12.

* Fri Jul 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.11-1
- Update to release 0.6.11.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Initial package. (using DAR)
