# $Id$
# Authority: dag

Summary: Hierarchical notebook
Name: hnb
Version: 1.9.18
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://hnb.sourceforge.net/

Source: http://hnb.sf.net/.files/hnb-%{version}.tar.gz
Patch0: hnb-1.9.18-optflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Hierarchical notebook(hnb) is a curses program to structure many kinds
of data in one place, for example addresses, to-do lists, ideas, book
reviews or to store snippets of brainstorming. Writing structured
documents and speech outlines.

The default format is XML but hnb can also export to ASCII and HTML.
External programs may be used for more advanced conversions of the XML
data.

%prep
%setup
%patch0

%build
%{__make} %{?_smp_mflags} OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/hnb %{buildroot}%{_bindir}/hnb
%{__install} -Dp -m0644 doc/hnb.1 %{buildroot}%{_mandir}/man1/hnb.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/*.html doc/hnbrc
%doc %{_mandir}/man1/hnb.1*
%{_bindir}/hnb

%changelog
* Fri Jun 16 2006 Dag Wieers <dag@wieers.com> - 1.9.18-1
- Initial package. (using DAR)
