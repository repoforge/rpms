# $Id$
# Authority: dries
# Upstream: Lee Goddard <lgoddard$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-Member

Summary: Member function of Prolog
Name: perl-List-Member
Version: 0.043
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-Member/

Source: http://www.cpan.org/modules/by-module/List/List-Member-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)

%description
PROLOG's member/2: return index of $x in @y.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/List::Member.3pm*
%dir %{perl_vendorlib}/List/
#%{perl_vendorlib}/List/Member/
%{perl_vendorlib}/List/Member.pm

%changelog
* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.043-1
- Updated to release 0.043.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.042-1
- Updated to release 0.042.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
