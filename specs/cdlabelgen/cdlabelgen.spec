# $Id$
# Authority: dag
# Upstream: Avinash Chopde <avinash$acm,org>

Summary: Generates frontcards and traycards for inserting in CD jewelcases
Name: cdlabelgen
Version: 4.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.aczoom.com/tools/cdinsert/

Source: http://www.aczoom.com/pub/tools/cdlabelgen-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
Cdlabelgen is a utility which generates frontcards and traycards
(in PostScript(TM) format) for CD jewelcases.

%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 cdlabelgen %{buildroot}%{_bindir}/cdlabelgen
%{__install} -Dp -m0644 cdlabelgen.1 %{buildroot}%{_mandir}/man1/cdlabelgen.1

%{__install} -d -m0755 %{buildroot}%{_datadir}/cdlabelgen/
%{__install} -p -m0644 postscript/* %{buildroot}%{_datadir}/cdlabelgen/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc cdlabelgen.html ChangeLog README
%doc %{_mandir}/man1/*.1*
%{_bindir}/cdlabelgen
%{_datadir}/cdlabelgen/

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 4.1.0-1
- Updated to release 4.1.0.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 3.6.0-1
- Initial package. (using DAR)
