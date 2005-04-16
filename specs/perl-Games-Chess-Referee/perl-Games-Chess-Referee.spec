# $Id$
# Authority: dries
# Upstream: Gregor N. Purdy <gregor$focusresearch,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-Chess-Referee

Summary: Work with chess positions and games, according to the rules of chess
Name: perl-Games-Chess-Referee
Version: 0.002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-Chess-Referee/

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GREGOR/Games-Chess-Referee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is an early conversion of my first chess-related Perl
program, chess.pl, which provided just enough functionality to
permit tracking the movements of pieces throughout a game. One
notable feature is the ability to provide incomplete ply notation,
allowing the program to figure out, for example, the type of the
piece being moved, or whether the ply represents a capture (x) or
occupation (-). This functionality will be broadened in the futuer
to permit partial space specification (e.g. `cxd4'), and other
cases of standard chess move notation.

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
%{perl_vendorlib}/Games/Chess/Referee.p*

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.002-1
- Initial package.
