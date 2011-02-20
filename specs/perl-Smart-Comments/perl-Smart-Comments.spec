# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Smart-Comments
%define real_version 1.000004

Summary: Perl module implements comments that do more than just sit there
Name: perl-Smart-Comments
Version: 1.0.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Smart-Comments/

Source: http://www.cpan.org/authors/id/D/DC/DCONWAY/Smart-Comments-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Smart-Comments is a Perl module implements comments
that do more than just sit there.

%prep
%setup -n %{real_name}-v%{version}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Smart::Comments.3pm*
%dir %{perl_vendorlib}/Smart/
%{perl_vendorlib}/Smart/Comments.pm

%changelog
* Sun Feb 20 2011 Denis Fateyev <denis@fateyev.com> - 1.0.4-1
- Updated to release 1.0.4.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
