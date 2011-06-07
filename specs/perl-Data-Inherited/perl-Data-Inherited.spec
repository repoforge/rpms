# $Id$
# Authority: shuff
# Upstream: Marcel Gruenauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Inherited

Summary: Hierarchy-wide accumulation of list and hash results
Name: perl-Data-Inherited
Version: 1.100860
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Inherited/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Data-Inherited-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(NEXT)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: perl(parent)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.0
Requires: perl(Carp)
Requires: perl(English)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(NEXT)
Requires: perl(Scalar::Util)
Requires: perl(Test::More)
Requires: perl(constant)
Requires: perl(overload)
Requires: perl(parent)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is a mixin class. By inheriting from it you get two methods that are able
to accumulate hierarchy-wide list and hash results.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\\.31.*/ && s/6\\.3\\d/6.30/' Makefile.PL}

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
%doc Changes INSTALL LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Data/Inherited.pm
# %{perl_vendorlib}/Data/Inherited/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Jun 07 2011 Steve Huff <shuff@vecna.org> - 100860-1
- Initial package.
