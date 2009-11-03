# $Id$
# Authority: dag
# Upstream: Suso Banderas <suso$suso,org>

Summary: Programs for dealing with numbers
Name: num-utils
Version: 0.5
Release: 2.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://suso.suso.org/programs/num-utils/

Source: http://suso.suso.org/programs/num-utils/downloads/num-utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
The num-utils, short for numeric utilities are a set of programs designed
to work together from the Unix shell to do numeric operations on input.
They are basically the numeric equivilent of common Unix text utilities
and aim to help complete the Unix shell vocabulary.

%prep
%setup

%{__perl} -pi.orig -e 's|use the|utilise the|g' *

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	DOCDIR="rpm-doc" \
	MANDIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-doc/* tests/
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-2.2
- Rebuild for Fedora Core 5.

* Sun Dec 05 2004 Dag Wieers <dag@wieers.com> - 0.5-2
- Workaround the idiotic perl-find-requires.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
