# $Id$
# Authority: dries
# Upstream: Gareth D. Rees <garethr$cre,canon,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-Chess

Summary: Represent chess positions and games
Name: perl-Games-Chess
Version: 0.003
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-Chess/

Source: http://search.cpan.org/CPAN/authors/id/G/GD/GDR/Games-Chess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The `Games::Chess' package provides the class
`Games::Chess::Piece' to represent chess pieces, and the class
`Games::Chess::Position' to represent a position in a chess
game. Objects can be instantiated from data in standard formats
and exported to these formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Games/Chess.p*
%{perl_vendorlib}/Games/Chess

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.003-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.003-1
- Initial package.
