# $Id: $

# Authority: dries
# Upstream: 

Summary: Very nasty tetris game
Name: bastet
Version: 0.37
Release: 1
License: GPL
Group: Amusements/Games
URL: http://fph.altervista.org/prog/bastet.shtml

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://fph.altervista.org/prog/bastet-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 

%description
Bastet (stands for "bastard tetris") is a free (GPL'd) clone of Tetris(r)
(built on the top of petris by Peter Seidler) which is designed to be "as
bastard as possible": it tries to compute how useful blocks are and gives
you the worst, the most bastard it can find. Playing bastet can be a painful
experience, especially if you usually make "canyons" and wait for the long
I-shaped block.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sun May 2 2004 Dries Verachtert <dries@ulyssis.org> - 
- Initial package.
