# $Id$

# Authority: dag

Summary: A set of programs for dealing with numbers.
Name: num-utils
Version: 0.3
Release: 0
License: GPL
Group: System Environment/Base
URL: http://suso.suso.org/programs/num-utils/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://suso.suso.org/programs/num-utils/downloads/%{name}-%{version}.tar.gz
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

%build
%{__make} %{?_smp_mpflags}

%install
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	DOCDIR="doc-rpm" \
	MANDIR="%{buildroot}%{_mandir}/man1"

%files
%defattr(-, root, root, 0755)
%doc doc-rpm/* tests/
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
