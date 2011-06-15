# $Id$
# Authority: shuff
# Upstream: Miguel Pignatelli <motif$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-File-AnyData

Summary: Access the data of a file via Perl array
Name: perl-Tie-File-AnyData
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-File-AnyData/

Source: http://search.cpan.org/CPAN/authors/id/M/MO/MOTIF/Tie-File-AnyData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Tie::File) >= 0.96
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Tie::File) >= 0.96

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module hacks 'Tie::File' to allow it to manage any kind of data. See the
documentation of 'Tie::File' for more details on the functionality of this
module.

To do so, you must provide a code reference (an anonymous subroutine) to the
tie call. This code should be able to read one record of your data file per
call.

There are already some modules that subclasses this one and provide examples of
use of this module. For example, check the documentation for
Tie::File::AnyData::Bio::Fasta or Tie::File::AnyData::MultiRecord_CSV. You can
use them as guidelines to build your own subroutines and modules. If you don't
know how to do that, but you are still interested in having a module that
manages your format of interest, contact me and I will do my best to help you
in the implementation.

This module keeps intact all the goodies that Tie::File offers (caching and
memory limits, deferred writing, etc). In fact you can safely use this module
with the default parameters instead of Tie::File without performance penalty.

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
%{perl_vendorlib}/Tie/File/AnyData.pm
#%{perl_vendorlib}/Tie/File/AnyData/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Wed Jun 15 2011 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
