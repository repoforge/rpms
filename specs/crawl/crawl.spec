# $Id$
# Authority: shuff
# Upstream: Crawl dev team <crawl-ref-discuss$lists,sourceforge,net>

%define real_name stone_soup
%define real_release 1
%define git_hash g7ce9b19

Summary: Dungeon Crawl Stone Soup (innovative roguelike game)
Name: crawl%{?_with_tiles:-tiles}
Version: 0.7.2
Release: 1%{?dist}
License: Crawl GPL (based on Nethack Licence)
Group: Applications/Games
URL: http://crawl.develz.org/

Source: http://downloads.sourceforge.net/project/crawl-ref/Stone%20Soup/%{version}/stone_soup-%{version}-nodeps.tar.bz2
Patch0: crawl-0.7.1_sqlite3.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: binutils
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: lua-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: sqlite-devel
%{?_with_tiles:BuildRequires: freetype-devel}
%{?_with_tiles:BuildRequires: libpng-devel}
%{?_with_tiles:BuildRequires: pkgconfig}
%{?_with_tiles:BuildRequires: zlib-devel}
%{?_with_tiles:BuildRequires: SDL-devel}
%{?_with_tiles:BuildRequires: SDL_image-devel}

# install only crawl or crawl-tiles
%{?_with_tiles:Conflicts: crawl}
%{!?_with_tiles:Conflicts: crawl-tiles}

%description
Dungeon Crawl Stone Soup is a free roguelike game of exploration and
treasure-hunting in dungeons filled with dangerous and unfriendly monsters in a
quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup has diverse species and many different character
backgrounds to choose from, deep tactical game-play, sophisticated magic,
religion and skill systems, and a grand variety of monsters to fight and run
from, making each game unique and challenging.

%{?_with_tiles:This package is compiled with tile graphics.}%{!?_with_tiles:This package is compiled with a character-based interface.}

Available rpmbuild rebuild optionms:
    --with: tiles

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%define mflags DESTDIR="%{buildroot}" prefix=%{_prefix} bin_prefix=/bin DATADIR=%{_datadir}/crawl/ SAVEDIR='~/.crawl' USE_UNICODE=y %{?_with_tiles:TILES=y SDL_INCLUDE='-I%{_includedir}/SDL'}
cd source
%{__make} %{?_smp_mflags} %{mflags}

%install
%{__rm} -rf %{buildroot}
cd source
%{__make} %{?_smp_mflags} %{mflags} install

# install the man page
cd ..
%{__install} -d -m0755 %{buildroot}%{_mandir}/man6
%{__install} -m0644 docs/crawl.6 %{buildroot}%{_mandir}/man6

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS.txt INSTALL.txt licence.txt README.pdf README.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/crawl/

%changelog
* Wed Mar 23 2011 Steve Huff <shuff@vecna.org> - 0.7.2-1
- Update to version 0.7.2.

* Thu Jul 29 2010 Steve Huff <shuff@vecna.org> - 0.7.1-1
- Initial package.
