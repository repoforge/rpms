# $Id$
# Authority: dries
# Upstream: Jeff Pinyan <japhy,734+CPAN$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-chmod

Summary: Implements symbolic and ls chmod modes
Name: perl-File-chmod
Version: 0.32
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-chmod/

Source: http://search.cpan.org/CPAN/authors/id/P/PI/PINYAN/File-chmod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Implements symbolic and ls chmod modes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/File::chmod.3*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/chmod.pm

%changelog
* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Initial package.
