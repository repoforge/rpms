# $Id$
# Authority: dag

Summary: Tool for generating simple man pages from program output
Name: help2man
Version: 1.38.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.gnu.org/software/help2man/

Source: http://ftp.gnu.org/gnu/help2man/help2man-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Locale::gettext)

%description
help2man is a tool for automatically generating simple manual pages
from program output.

It is intended to provide an easy way for software authors to include
a manual page in their distribution without having to maintain that
document.

Given a program which produces resonably standard --help and --version
outputs, help2man will attempt to re-arrange that output into
something which resembles a manual page.

%prep
%setup

%build
%configure --libdir="%{_libdir}/help2man"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING NEWS README THANKS
%doc %{_infodir}/help2man.info*
%doc %{_mandir}/man1/help2man.1*
%doc %{_mandir}/*/man1/help2man.1*
%{_bindir}/help2man
%{_libdir}/help2man/bindtextdomain.so

%changelog
* Thu Sep 23 2010 Dag Wieers <dag@wieers.com> - 1.38.2-1
- Initial package. (using DAR)
