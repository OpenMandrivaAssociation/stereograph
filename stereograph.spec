%define name    stereograph 
%define version 0.33b
%define release %mkrel 5

Name:           %{name} 
Summary:        Stereograph for linux, an advanced stereogram generator 
Version:        %{version} 
Release:        %{release} 
Source0:        http://download.sourceforge.net/stereograph/%{name}-%{version}.tar.bz2 
Patch0:         %name-makefile.patch
URL:            http://stereograph.sourceforge.net/
Group:          Graphics 
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
License:        GPL 


BuildRequires:  X11-devel
BuildRequires:  jpeg-devel
BuildRequires:  png-devel


%description
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That's a program that produces twodimensional
images that seem to be threedimensional (surely you know the famous works of
"The Magic Eye", Stereograph produces the same output). You do _not_ need
any pair of colored spectacles to regard them - everyone can learn it.

%prep 
%setup -q  
%patch0 -p0

%build 
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make install PREFIX=$RPM_BUILD_ROOT/usr 

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_mandir}/man1/stereograph*
%{_bindir}/stereograph 



