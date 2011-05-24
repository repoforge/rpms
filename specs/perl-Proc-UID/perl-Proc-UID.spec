# $Id$
# Authority: shuff
# Upstream: Paul Jamieson Fenwick <pjf$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-UID

Summary: Manipulate a variety of UID and GID settings
Name: perl-Proc-UID
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-UID/

Source: http://search.cpan.org/CPAN/authors/id/P/PJ/PJF/Proc-UID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildArch: noarch
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl >= 5.6.0
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.6.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl only has concepts of effective and real user-ids (UIDs) and group-ids
(GIDs), accessible via the special variables $<, $>, $( and $). However most
modern Unix systems also have a concept of saved UIDs.

This module provides a consistent and logical interface to real, effective, and
saved UIDs and GIDs. It also provides a way to permanently drop privileges to
that of a given user, a process which $< = $> = $uid does not guarantee, and
the exact syntax of which may vary from between operating systems.

Proc::UID is also very pedantic about making sure that operations succeeded,
and checking the value which it returns for a UID/GID really is the one that's
being used. Perl may sometimes cache the values of $<, $>, $( and $), which
means they can be wrong after being changed with low-level system calls.

Proc::UID provides both a variable and function interfaces to underlying UIDs.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Proc/UID.pm
%{perl_vendorarch}/auto/Proc/UID/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue May 24 2011 Steve Huff <shuff@vecna.org> - 0.05-1
- Initial package.
