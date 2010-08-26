# $Id$
# Authority: shuff
# Upstream: Philip Gwyn <gwyn$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Diff-Parser

Summary: Parse patches containing unified and standard diffs
Name: perl-Text-Diff-Parser
Version: 0.1001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Diff-Parser/

Source: http://search.cpan.org/CPAN/authors/id/G/GW/GWYN/Text-Diff-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Text::Diff::Parser parses diff files and patches. It allows you to access the
changes to a file in a standardized way, even if multiple patch formats are
used.

A diff may be viewed a series of operations on a file, either adding, removing
or modifying lines of one file (the from-file) to produce another file (the
to-file). Diffs are generaly produced either by hand with diff, or by your
version control system (cvs diff, svn diff, ...). Some diff formats, notably
unified diffs, also contain null operations, that is lines that

Text::Diff::Parser currently parses unified diff format and standard diff
format.

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
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Text/Diff/Parser.pm
#%{perl_vendorlib}/Text/Diff/Parser/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Aug 26 2010 Steve Huff <shuff@vecna.org> - 0.1001-1
- Initial package.
