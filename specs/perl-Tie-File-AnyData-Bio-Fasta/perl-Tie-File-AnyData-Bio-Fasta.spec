# $Id$
# Authority: shuff
# Upstream: Miguel Pignatelli <motif$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-File-AnyData-Bio-Fasta

Summary: Accessing fasta records in a file via Perl array
Name: perl-Tie-File-AnyData-Bio-Fasta
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-File-AnyData-Bio-Fasta/

Source: http://search.cpan.org/CPAN/authors/id/M/MO/MOTIF/Tie-File-AnyData-Bio-Fasta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Tie::File::AnyData) >= 0.01
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Tie::File::AnyData) >= 0.01

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Tie::File::AnyData::Bio::Fasta allows the management of fasta files via a Perl
array through Tie::File::AnyData, so read the documentation of this module for
further details on its internals.

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
%{perl_vendorlib}/Tie/File/AnyData/Bio/Fasta.pm
#%{perl_vendorlib}/Tie/File/AnyData/Bio/Fasta*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/*/*/.packlist

%changelog
* Wed Jun 15 2011 Steve Huff <shuff@vecna.org> - 0.01-1
- Initial package.
