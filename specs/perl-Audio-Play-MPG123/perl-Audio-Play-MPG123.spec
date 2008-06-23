# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-Play-MPG123

Summary: Frontend to mpg123
Name: perl-Audio-Play-MPG123
Version: 0.63
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-Play-MPG123/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-Play-MPG123-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a frontend to the mpg123 player. It works by starting an
external mpg123 process with the "-R" option and feeding commands to it.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Audio/Play/MPG123.pm
%{_bindir}/mpg123sh

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Initial package.
