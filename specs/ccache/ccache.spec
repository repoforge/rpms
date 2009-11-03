# $Id$
# Authority: dag
# Upstream: Andrew Tridgell <tridge$samba,org>

Summary: Compiler cache
Name: ccache
Version: 2.4
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://ccache.samba.org/

Source: http://samba.org/ftp/ccache/ccache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gcc, gcc-c++

%description
ccache is a compiler cache. It acts as a caching pre-processor to
C/C++ compilers, using the -E compiler switch and a hash to detect
when a compilation can be satisfied from cache. This often results in
a 5 to 10 times speedup in common compilations.

%prep
%setup

%{__cat} <<'EOF' >ccache.sh
if [ -x "%{_bindir}/ccache" -a -d "%{_libdir}/ccache/bin" ]; then
	if ! echo "$PATH" | grep -q %{_libdir}/ccache/bin; then
		PATH="%{_libdir}/ccache/bin:$PATH"
	fi
fi
EOF

%{__cat} <<'EOF' >ccache.csh
if ( "$path" !~ *%{_libdir}/ccache/bin* ) then
	set path = ( %{_libdir}/ccache/bin $path )
endif
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0755 ccache.csh %{buildroot}%{_sysconfdir}/profile.d/ccache.csh
%{__install} -Dp -m0755 ccache.sh %{buildroot}%{_sysconfdir}/profile.d/ccache.sh

%{__install} -d -m0755 %{buildroot}%{_libdir}/ccache/bin/
for compiler in cc c++ gcc g++ gcc296 g++296; do
    %{__ln_s} -f %{_bindir}/ccache %{buildroot}%{_libdir}/ccache/bin/$compiler
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/profile.d/*
%{_bindir}/*
%{_libdir}/ccache/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.4-1
- Updated to release 2.4.

* Sun Sep 28 2003 Dag Wieers <dag@wieers.com> - 2.3-0
- Updated to release 2.3.

* Sat May 10 2003 Dag Wieers <dag@wieers.com> - 2.2-1
- Fixed ccache.sh/ccache.csh. (Thomas Moschny)

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Initial package. (using DAR)
