# Authority: dag

Summary: An OpenGL 3D modeller and renderer.
Name: moonlight
Version: 0.5.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.moonlight3d.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ml3d.sourceforge.net/install/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: freetype-devel

%description
Moonlight|3D is a free software modeller and renderer for 3D scenes
with an intuitive GUI and powerful editing capabilities.

%prep
%setup -n %{name}

%build
cd src/
%configure \
	--with-ttf-include="%{_includedir}/freetype1/freetype"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README
%{_bindir}/*
%{_datadir}/moonlight/

%changelog
* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.5.5-0
- Initial package. (using DAR) 
