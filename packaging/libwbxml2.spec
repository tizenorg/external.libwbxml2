%define _name libwbxml
Name: libwbxml2
Version: 0.11.0
Release: 10
Summary: Library to parse, encode and handle WBXML documents
Group: System/Libraries
License: LGPLv2.1
Source0: %{name}-%{version}.tar.gz
BuildRequires: expat-devel zlib-devel popt-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake

%description
The WBXML Library (aka libwbxml) contains a library and its associated
tools to Parse, Encode and Handle WBXML documents.  The WBXML format
is a binary representation of XML, defined by the Wap Forum, and used
to reduce bandwidth in mobile communications.


%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package utils
Summary: Binary XML utilities %{name}-utils
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description utils    
This package is libwbxml2-utils pkg for libwbxml2  

%prep
%setup -q
mkdir build

%build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
cd build
%make_install


%clean
cd build
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*.so.*
%doc %{_docdir}/*

%files devel
%defattr(-,root,root,-)
/usr/include/libwbxml-1.0/wbxml/*.h
/usr/include/wbxml_config.h
/usr/lib/libwbxml2.so
/usr/lib/pkgconfig/libwbxml2.pc

%files utils
%defattr(-,root,root,-)
%{_bindir}/*

