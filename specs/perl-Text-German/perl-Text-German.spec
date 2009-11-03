# $Id$
# Authority: dries
# Upstream: Ulrich Pfeifer <pfeifer$wait,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-German

Summary: German grundform reduction
Name: perl-Text-German
Version: 0.06
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-German/

Source: http://www.cpan.org/modules/by-module/Text/Text-German-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a rather incomplete implementaion of work done by
Gudrun Putze-Meier <gudrun.pm@t-online.de>. I have to
confess that I never read her original paper. So all
credit belongs to her, all bugs are mine. I tried to get
some insight from an implementation of two students of
mine. They remain anonymous because their work was the
wost piece of code I ever saw. My code behaves mostly as
their implementation did except it is about 75 times
faster.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/German.p*
%{perl_vendorlib}/Text/German/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
