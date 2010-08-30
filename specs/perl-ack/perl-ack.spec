# $Id$
# Authority: shuff
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ack

Summary: A grep-like program specifically for large source trees
Name: perl-ack
Version: 1.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://betterthangrep.com/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/ack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Next) >= 0.4
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::Harness) >= 2.5
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(File::Basename)
Requires: perl(File::Next) >= 0.4
Requires: perl(Getopt::Long)
Requires: perl(Pod::Usage)
Requires: perl(Term::ANSIColor)

Provides: ack = %{version}
Provides: %{_bindir}/ack

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Ack is designed as a replacement for 99% of the uses of grep.

Ack searches the named input FILEs (or standard input if no files are named, or
the file name - is given) for lines containing a match to the given PATTERN. By
default, ack prints the matching lines.

Ack can also list files that would be searched, without actually searching
them, to let you take advantage of ack's file-type filtering capabilities.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/App/Ack.pm
%{perl_vendorlib}/App/Ack/*
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Mon Aug 30 2010 Steve Huff <shuff@vecna.org> - 1.92-1
- Initial package.
